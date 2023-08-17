from django.urls import path
from checkouts.api.views import CheckoutView, CheckoutViewById

urlpatterns = [
    path('checkout/', CheckoutView.as_view()),
    path('checkout/<int:id>/', CheckoutViewById.as_view(), name='checkout_by_id'),
]