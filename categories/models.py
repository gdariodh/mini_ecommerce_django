from django.db import models
from django.db.models.deletion import SET_NULL
from users.models import User

class Category(models.Model):
    name = models.CharField(unique=True,max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name
    
