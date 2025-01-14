# Wafer apps for DebConf

This package contains several Django apps used by the DebConf
conference.

## badges - Name tag generation

## bursary - Bursary requests and review

## debconf - Random bits and pieces

## exports - CSV data exports for organisers

## front\_desk - Check-In

## invoices - Paid Attendee Invoicing

## register - Attendee Registration

## volunteers - On-site volunteer wrangling

# Configuration

Uses the following Django settings:

Invoicing:

* `DEBCONF_INVOICE_ADDRESS`: String. Postal address to issue invoices from.
* `DEBCONF_BILLING_CURRENCY_SYMBOL`: String. The billing currency symbol. (e.g. $)
* `DEBCONF_BILLING_CURRENCY`: String. The billing currency code. (e.g.  USD)
* `DEBCONF_BURSARY_CURRENCY_SYMBOL`: String. The bursary currency symbol. (e.g. $)
* `DEBCONF_BURSARY_CURRENCY`: String. The bursary currency code (e.g.  USD)
* `DEBCONF_LOCAL_CURRENCY_RATE`: Decimal. The exchange rate. What does 1 DEBCONF_BILLING_CURRENCY buy in local currency.
* `DEBCONF_LOCAL_CURRENCY_SYMBOL`: String. The local currency symbol.
* `DEBCONF_LOCAL_CURRENCY`: String. The local currency code.
* `INVOICE_PREFIX`: String. Prefix to invoice IDs.
* `PRICES`: Dict of Dicts, with purchasable items and prices.
  * `fee`: Dict of conferences fees, each having a `name` and `price`.
  * `meal`: Dict of Dicts, (`breakfast`, `lunch`, `dinner`, `conference_dinner`):
    * Each having a `price` and optional `name`.
  * `accomm`: Dict of Dicts, (`description` (String), `price` (Decimal/int) per night, `bursary` (bool), `paid_separately` (bool), `included_meals` (set of strs)) for each accommodation option. If an option has a price, it's for sale. If bursary, it'll be available for free for bursaried attendants.
* `STRIPE_PUBLISHABLE_KEY`: String. Stripe API Publishable Key.
* `STRIPE_SECRET_KEY`: String. Stripe API Secret Key.
* `STRIPE_ENDPOINT_SECRET`: String. Stripe Webhook endpoint secret.

Dates:

* `DEBCONF_BURSARY_DEADLINE`: Date. The date that bursaries need to be submitted by, AoE
* `DEBCONF_BURSARY_ACCEPTANCE_DEADLINE`: Date. The date that all bursaries need to be accepted by, or the attendee will be issued an invoice.
* `DEBCONF_CONFERENCE_DINNER_DAY`: Date. The day that has the conference dinner.
* `DEBCONF_CONFIRMATION_DEADLINE`: Date. The date that attendance needs to be confirmed by, AoE.
* `DEBCONF_DATES`: List of (Description, Start Date, End Date) for the parts of the conference.
* `DEBCONF_SKIPPED_MEALS`: List of (String: meal name, Date) of meals that will not be provided.
* `VOLUNTEERS_FIRST_DAY`: Date. The first day of volunteering.
* `VOLUNTEERS_LAST_DAY`: Date. The last day of volunteering.

Registration:

* `BURSARIES_CLOSED`: Boolean. Can bursary requests still be submitted.
* `DEBCONF_BREAKFAST`: Boolean. Is DebConf providing breakfast for attendees.
* `DEBCONF_SHOE_SIZES`: List of (Key, Description) for Shoe sizes.
* `DEBCONF_T_SHIRT_SIZES`: List of (Key, Description) for T-Shirt sizes.
* `RECONFIRMATION`: Boolean. Is there a reconfirmation round (set True once it has started).
* `DEBCONF_REVIEW_FREE_ATTENDEES`: Boolean. Use the bursary system to review the attendance of free attendees too.
* `MINIDEBCONF_REGISTER_PHONE`: for minidebconfs, whether to ask for phone
  numbers upon registration. Values:
  - `None` - don't ask (default)
  - `False` - ask but not require
  - `True` - ask and require

Content:

* `TRACKS_FILE`: String. path to a YAML file with the list of tracks to be loadede into the database
* `TALK_TYPES_FILE`: String. path to a YAML file with the list of talk types to be loaded into the database
* `DEBCONF_TALK_PROVISION_URLS`: Dictionary of {Key: {pattern: String, private: Boolean}} for online services to generate links for. Format string parameters available: `id`, `slug`, `secret16`).

Misc:

* `DEBCONF_CITY`: String. The name of the city hosting DebConf.
* `DEBCONF_NAME`: String. The name of the Debconf (e.g. "DebConf XX").
* `DCSCHEDULE_TOKEN`: String. Authentication token for the DCSchedule IRC bot to hit the API.
* `SANDBOX`: Boolean. Is this a development instance or production.
* `ISSUE_KSP_ID`: Boolean. Is the key-signing sign-up still open?

Streaming:

* `DEBCONF_VENUE_STREAM_HLS_URL`: String. URL to the HLS stream. {name}, if
  present, is replaced with with the venue name in lower case and with all
  sequences of non-alphanumeric characters replaced with a "-". Examples:
  - Fixed URL: `"https://foo.bar/stream.m3u8"` (good enough for single-venue
    conferences.)
  - Per-venue URL: `"https://foo.bar/stream/{name}.m3u8"` becomes
    `"https://foo.bar/stream/my-venue.m3u8"`
* `DEBCONF_VENUE_STREAM_RTMP_URL` String. URL to the RTMP stream. {name} is
  substituted as with `DEBCONF_VENUE_STREAM_HLS_URL`; {quality} is replaced with
  the quality (src, high, mid, low). Examples:
  - Fixed URL: `"rtmp://foo.bar/stream"` (for single-venue conferences)
  - Per-venue URL: `"rtmp://foo.bar/stream/{name}_{quality}"` becomes
    `"rtmp://foo.bar/stream/my-venue_high"` ("high" quality stream for "My
    Venue")
* `DEBCONF_VENUE_IRC_CHANNELS`: List of strings. List of channels to join for
  each venue; {name} is replaced as above. Examples:
  - Single-channel conference: `["#conference"]`
  - Multi-venue conference: `["#thatconf2020-{name}",  "#thatconf2020"]`
    becomes `["#thatconf2020-my-venue", "#thatconf2020"]`

## Stripe Payments

First, configure the `STRIPE_PUBLISHABLE_KEY` and `STRIPE_SECRET_KEY`
settings, with the API keys from the Stripe dashboard.

To receive payment confirmation from Stripe, we need to receive a
webhook from them.

For local development, you can receive this with the [stripe
CLI](https://github.com/stripe/stripe-cli):

```
$ stripe login
...
$ stripe listen --forward-to http://127.0.0.1:8000/invoices/stripe-webhook/
> Ready! Your webhook signing secret is whsec_I_AM_A_SECRET_KEY (^C to quit)
```

Configure `STRIPE_ENDPOINT_SECRET` with the secret key provided by
`stripe-cli listen`.

For production use, configure a webhook in the Stripe dashboard.
The endpoint should be `https://my.debconf/invoices/stripe-webhook/`.
Listen for `charge.dispute.created`,  `charge.refunded`, and
`payment_intent.succeeded`.
Again, `STRIPE_ENDPOINT_SECRET` should be configured to the webhook's
signing secret.
