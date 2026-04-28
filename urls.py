from django.urls import path
from .views import CheckoutView, stripe_webhook

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='stripe-checkout'),
    path('webhook/', stripe_webhook, name='stripe-webhook'),
]
