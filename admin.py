from django.contrib import admin
from .models import Subscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'stripe_customer_id', 'current_period_end')
    readonly_fields = ('stripe_customer_id', 'stripe_subscription_id')
