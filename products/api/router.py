from django.urls import path
from products.api.views import ProductView, ProductViewById, ProductViewByUser

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<int:id>', ProductViewById.as_view()),
    path('products/user/<int:id>', ProductViewByUser.as_view()),
]