from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
from users.models import User
from products.models import Product
from products.api.serializers import CreateProductSerializer, ProductSerializer

class CreateProductView(APIView):
    
    def post(self, request):
        serializer = CreateProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class GetProductView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = CreateProductSerializer(products, many=True)
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

class GetProductByIdView(APIView):
    
        def get(self, request, id):
              
            try:
                product = Product.objects.get(id=id)
                serializer = CreateProductSerializer(product)
                return Response(status=status.HTTP_201_CREATED, data=serializer.data)
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={
                    'message': 'Product not found'
                })

class GetProductsByUser(APIView):
        
        def get(self, request, id):
            try:
                products = Product.objects.filter(user_id=id)
                serializer = CreateProductSerializer(products, many=True)
                return Response(status=status.HTTP_201_CREATED, data=serializer.data)
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={
                    'message': 'Products not found'
                })
    

   
    
        
    
