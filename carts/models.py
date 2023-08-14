from django.db import models
from products.models import Product
from users.models import User

class Cart(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    