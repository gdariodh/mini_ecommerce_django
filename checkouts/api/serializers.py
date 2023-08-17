from rest_framework import serializers
from checkouts.models import Checkout
from users.api.serializers import UserSerializer
from carts.api.serializers import CartSerializerSummary

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ['id', 'cart', 'user', 'paid', 'amount', 'shipping_address', 'stripe_charge_id', 'created_at']


class CheckoutSerializerSummary(serializers.ModelSerializer):

    cart = CartSerializerSummary()
    user = UserSerializer()

    class Meta:
        model = Checkout
        fields = ['id', 'cart', 'user', 'paid', 'amount', 'shipping_address', 'stripe_charge_id', 'created_at']
