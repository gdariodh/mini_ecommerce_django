from django.db import models
from users.models import User
from carts.models import Cart
from products.models import Product
from products.api.serializers import ProductSerializer

class Checkout(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, unique=True)
    stripe_charge_id = models.CharField(max_length=50, null=True, unique=True)
    paid = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    shipping_address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.user} - {self.created_at}'
    
    def calculate_amount(self, cart_id):
            products = Product.objects.filter(cart=cart_id)
            products_serializer = ProductSerializer(products, many=True)
            amount = 0

            for product in products_serializer.data:
                amount += product['price']

            return amount 
    
    
    