from collections import OrderedDict

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from bursary.models import Bursary
from debconf.models import GENDERS
from debconf.tz import aoe_datetime
from register.fields import OptionalCountries


def build_fees():
    fees = []
    for id_, details in sorted(settings.PRICES['fee'].items(),
                               key=lambda fee: fee[1]['price']):
        price = details['price']
        if price:
            description = '{name} - {billing_price} {billing_currency}'
            if (settings.DEBCONF_BILLING_CURRENCY
                    != settings.DEBCONF_LOCAL_CURRENCY):
                description += ' or {local_price} {local_currency}'
        else:
            description = '{name} - Free'
        description = description.format(
            name=details['name'],
            billing_price=price,
            billing_currency=settings.DEBCONF_BILLING_CURRENCY,
            local_price=price * settings.DEBCONF_LOCAL_CURRENCY_RATE,
            local_currency=settings.DEBCONF_LOCAL_CURRENCY,
        )
        fees.append((id_, description))
    return OrderedDict(fees)


class Attendee(models.Model):
    FEES = build_fees()
    GENDERS = GENDERS

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='attendee',
                                on_delete=models.PROTECT)

    # Contact information
    nametag_2 = models.CharField(max_length=50, blank=True)
    nametag_3 = models.CharField(max_length=50, blank=True)
    emergency_contact = models.TextField(blank=True)
    announce_me = models.BooleanField()
    register_announce = models.BooleanField()
    register_discuss = models.BooleanField()

    # Conference details
    coc_ack = models.BooleanField(default=False)
    fee = models.CharField(max_length=5, blank=True)
    arrival = models.DateTimeField(null=True, blank=True)
    departure = models.DateTimeField(null=True, blank=True)
    final_dates = models.BooleanField(default=False)
    reconfirm = models.BooleanField(default=False)

    # Personal information
    t_shirt_size = models.CharField(max_length=8, blank=True)
    shoe_size = models.CharField(max_length=8, blank=True)
    gender = models.CharField(max_length=1, blank=True)
    country = models.CharField(max_length=2, blank=True)
    languages = models.CharField(max_length=50, blank=True)
    pgp_fingerprints = models.TextField(blank=True)

    # COVID-19
    vaccinated = models.BooleanField(null=True)
    vaccination_notes = models.TextField(blank=True)
    confirm_covid_tests = models.BooleanField(null=True)

    # Billing
    invoiced_entity = models.TextField(blank=True)
    billing_address = models.TextField(blank=True)

    # Misc
    notes = models.TextField(blank=True)
    completed_register_steps = models.IntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    completed_timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return 'Attendee <{}>'.format(self.user.username)

    def billable(self):
        """Is this user billable? (or paid)"""
        try:
            bursary = self.user.bursary
        except Bursary.DoesNotExist:
            bursary = Bursary()

        if self.fee:
            return True

        try:
            if (self.food.meals.exists()
                    and not bursary.potential_bursary('food')):
                return True
        except ObjectDoesNotExist:
            pass

        try:
            if (self.accomm.nights.exists()
                    and not bursary.potential_bursary('accommodation')):
                return True
        except ObjectDoesNotExist:
            pass

        return False

    billable.boolean = True

    def paid(self):
        from invoices.prices import invoice_user
        invoices = self.user.invoices
        if invoices.filter(status='new').exists():
            return False

        invoice = invoice_user(self.user)
        return invoice['total'] <= 0

    paid.boolean = True

    def registered_before_deadline(self):
        if not self.completed_timestamp:
            return False
        return (
            self.completed_timestamp <
            aoe_datetime(settings.DEBCONF_CONFIRMATION_DEADLINE))

    registered_before_deadline.boolean = True

    def registration_approved(self):
        if not settings.DEBCONF_REVIEW_FREE_ATTENDEES:
            return True
        if self.billable() and self.paid():
            return True
        try:
            bursary = self.user.bursary
        except Bursary.DoesNotExist:
            bursary = Bursary()
        if bursary.status_in(None, 'accepted'):
            return True
        if bursary.attendance_status in ('accepted', 'pending'):
            return True
        return False

    registration_approved.boolean = True

    @property
    def new_invoices(self):
        return self.user.invoices.filter(status='new')

    def queue_position(self, name):
        from register.models.queue import QueueSlot
        try:
            slot = QueueSlot.objects.get(queue__name=name, attendee=self)
            return slot.monotonic_position
        except QueueSlot.DoesNotExist:
            return None

    @property
    def keysigning_id(self):
        return self.queue_position('PGP Keysigning')

    @property
    def registration_queue_slot(self):
        return self.queue_position('Registration')

    @property
    def arrived(self):
        try:
            self.check_in
            return True
        except ObjectDoesNotExist:
            return False

    @property
    def country_name(self):
        return OptionalCountries().name(self.country)

    @property
    def shipping_address(self):
        from register.models.address import Address
        try:
            return Address.objects.get(attendee=self, role='shipping')
        except Address.DoesNotExist:
            return None

    def save(self, *args, **kwargs):
        if self.arrival == '':
            self.arrival = None
        if self.departure == '':
            self.departure = None
        return super().save(*args, **kwargs)
