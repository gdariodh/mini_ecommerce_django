from django.urls import path
from carts.api.views import CartView, CartViewById

urlpatterns = [
    path('carts/', CartView.as_view()),
    path('carts/<int:id>', CartViewById.as_view(), name='cart-detail'),
]