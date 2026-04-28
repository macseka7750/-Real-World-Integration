import stripe
from django.conf import settings

def verify_stripe_webhook(payload, sig_header):
    """Verifies the authenticity of a Stripe webhook request."""
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
        return event
    except (ValueError, stripe.error.SignatureVerificationError):
        return None
