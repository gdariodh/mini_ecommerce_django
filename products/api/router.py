from django.urls import path
from products.api.views import CreateProductView, GetProductView, GetProductByIdView

urlpatterns = [
    path('products/create', CreateProductView.as_view()),
    path('products/', GetProductView.as_view()),
    path('products/<int:id>', GetProductByIdView.as_view()),
]