from django.contrib import admin
from checkouts.models import Checkout

@admin.register(Checkout)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'paid', 'amount', 'shipping_address', 'user')
