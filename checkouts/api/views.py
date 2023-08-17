from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from checkouts.models import Checkout
from checkouts.api.serializers import CheckoutSerializer, CheckoutSerializerSummary

# /checkout
class CheckoutView(APIView):
    def get(self, request):
        try:
            checkouts = Checkout.objects.all().order_by("-created_at")
            serializer = CheckoutSerializer(checkouts, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"message": "There was a problem"},
            )

    def post(self, request):
        try:
            req_data = request.data
            cart_id, user_id = req_data["cart"], req_data["user"]

            amount = Checkout().calculate_amount(cart_id)

            data = {
                "amount": amount,
                "cart": cart_id,
                "user": user_id,
            }

            serializer = CheckoutSerializer(data=data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(status=status.HTTP_201_CREATED, data=serializer.data)

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"message": "There was a problem"},
            )


class CheckoutViewById(APIView):
    def get(self, request, id):
        try:
            checkout = Checkout.objects.get(id=id)
            serializer = CheckoutSerializerSummary(checkout)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"message": f"Checkout not found, id: {id}"},
            )

    def put(self, request, id):
        try:
            req_data = request.data
            user_id, shipping_address = (
                req_data["user"],
                req_data["shipping_address"],
            )

            checkout = Checkout.objects.get(id=id)

            data = {
                "user": user_id,
                "shipping_address": shipping_address,
                "cart": checkout.cart.id,
            }

            serializer = CheckoutSerializer(checkout, data=data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(status=status.HTTP_201_CREATED, data=serializer.data)

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"message": f"Checkout not found, id: {id}"},
            )

    def delete(self, request, id):
        try:
            checkout = Checkout.objects.get(id=id)
            checkout.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"message": f"Checkout not found, id: {id}"},
            )        
