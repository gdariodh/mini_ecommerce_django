from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from carts.api.serializers import CartSerializer, CartSerializerSummary
from carts.models import Cart

# /carts
class CartView(APIView):
    
    def get(self, request):
        try:
            carts = Cart.objects.all().order_by('-created_at')
            serializer = CartSerializerSummary(carts, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={
                    'message': 'There was a problem'
             })
     
    
    def post(self, request):

        serializer = CartSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# /carts/<int:id>
class CartViewById(APIView):

    def get(self, request, id):

        try: 
            cart = Cart.objects.get(id=id)
            serializer = CartSerializerSummary(cart)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={
                    'message': 'Cart not found'
             })

    def put(self, request, id):

        try:
            cart = Cart.objects.get(id=id)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(cart, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            cart = Cart.objects.get(id=id)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data={
                    'message': 'cart not found'
            })
            
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
