from rest_framework import serializers
from carts.models import Cart
from products.api.serializers import ProductSerializerSummary

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'created_at', 'products', 'user']


class CartSerializerSummary(serializers.ModelSerializer):

    products = ProductSerializerSummary(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'created_at', 'products', 'user']
