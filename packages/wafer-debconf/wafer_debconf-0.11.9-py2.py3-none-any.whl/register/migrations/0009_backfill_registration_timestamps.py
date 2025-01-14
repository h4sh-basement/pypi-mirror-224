# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-07-16 12:50
from __future__ import unicode_literals

from django.db import migrations

from register.views import STEPS


def backfill_registration_timestamps(apps, schema_editor):
    last_step = len(STEPS) - 1
    Attendee = apps.get_model('register', 'Attendee')

    for attendee in Attendee.objects.filter(
            completed_register_steps=last_step,
            completed_timestamp__isnull=True):
        # Avoid using .save() so we don't touch updated_timestamp
        Attendee.objects.filter(id=attendee.id).update(
            completed_timestamp=attendee.updated_timestamp,
        )


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_backfill_registration_timestamps'),
    ]

    operations = [
        migrations.RunPython(backfill_registration_timestamps, noop),
    ]
