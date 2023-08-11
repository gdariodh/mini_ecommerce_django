from rest_framework import serializers
from products.models import Product

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'image', 'created_at', 'published', 'user', 'slug']

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'image', 'created_at', 'published', 'user', 'slug']