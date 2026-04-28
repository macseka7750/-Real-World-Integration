from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .services import StripeService
from .utils import verify_stripe_webhook
from .models import Subscription

class CheckoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        success_url = "http://localhost:3000/success?session_id={CHECKOUT_SESSION_ID}"
        cancel_url = "http://localhost:3000/cancel"
        
        session = StripeService.create_checkout_session(request.user, success_url, cancel_url)
        return Response({'url': session.url})

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    
    event = verify_stripe_webhook(payload, sig_header)
    if not event:
        return HttpResponse(status=400)

    # Handle the specific event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        # Logic to upgrade user role
        sub = Subscription.objects.get(stripe_customer_id=session.customer)
        sub.status = 'active'
        sub.stripe_subscription_id = session.subscription
        sub.save()
        
        # Upgrade the Custom User Role
        user = sub.user
        user.role = 'PREMIUM'
        user.save()

    return HttpResponse(status=200)
