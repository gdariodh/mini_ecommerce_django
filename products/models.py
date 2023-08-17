from django.db import models
from django.db.models.deletion import SET_NULL
from users.models import User
from categories.models import Category

class Product(models.Model):
    name = models.CharField(unique=True,max_length=255)
    price = models.IntegerField()
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='products/images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    slug = models.SlugField(unique=True, null=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.name

    def summary(self):
        return self.description[:100]

    def price_in_dollars(self):
        return '${}'.format(self.price)
    
