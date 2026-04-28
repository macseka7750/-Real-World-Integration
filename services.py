import stripe
from django.conf import settings
from .models import Subscription

stripe.api_key = settings.STRIPE_SECRET_KEY

class StripeService:
    @staticmethod
    def create_checkout_session(user, success_url, cancel_url):
        """Creates a secure Stripe Checkout session for the user."""
        # Check if user already has a customer ID, if not, create one
        sub, created = Subscription.objects.get_or_create(user=user)
        
        if not sub.stripe_customer_id:
            customer = stripe.Customer.create(email=user.email)
            sub.stripe_customer_id = customer.id
            sub.save()

        session = stripe.checkout.Session.create(
            customer=sub.stripe_customer_id,
            payment_method_types=['card'],
            line_items=[{
                'price': 'price_H5ggH9B16TR95s', # Replace with your real Stripe Price ID
                'quantity': 1,
            }],
            mode='subscription',
            success_url=success_url,
            cancel_url=cancel_url,
        )
        return session
