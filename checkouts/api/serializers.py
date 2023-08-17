from rest_framework import serializers
from checkouts.models import Checkout
from users.api.serializers import UserSerializer
from carts.api.serializers import CartSerializer

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ['id', 'cart', 'user', 'paid', 'amount', 'shipping_address', 'stripe_charge_id', 'created_at']


class CheckoutSerializerSummary(serializers.ModelSerializer):

    cart = CartSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Checkout
        fields = ['id', 'cart', 'user', 'paid', 'amount', 'shipping_address', 'stripe_charge_id', 'created_at']
