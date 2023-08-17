from django.contrib import admin
from carts.models import Cart

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'user')
