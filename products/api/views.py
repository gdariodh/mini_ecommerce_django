from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.api.permissions import IsStaffOrReadOnly
from products.models import Product
from products.api.serializers import CreateProductSerializer, ProductSerializer

# products/ 
class ProductView(APIView):
    permission_classes = [IsStaffOrReadOnly]

    def post(self, request):
        serializer = CreateProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        products = Product.objects.all().order_by('-created_at')
        serializer = ProductSerializer(products, many=True)
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
    

# products/<int:id>
class ProductViewById(APIView):
        
        permission_classes = [IsStaffOrReadOnly]
    
        def get(self, request, id):
            try:
                product = Product.objects.get(id=id)
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={
                    'message': 'Product not found'
                })
            
            serializer = ProductSerializer(product)

            return Response(status=status.HTTP_201_CREATED, data=serializer.data)    
            
        def put(self, request, id):

            try:
                product = Product.objects.get(id=id)
            except Exception as e:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = ProductSerializer(product, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def delete(self, request, id):
            try:
                product = Product.objects.get(id=id)
            except Exception as e:
                return Response(status=status.HTTP_404_NOT_FOUND, data={
                    'message': 'Product not found'
                })
            
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
# products/user/<int:id>
class ProductViewByUser(APIView):
        
        permission_classes = [IsStaffOrReadOnly]
        
        def get(self, request, id):
            try:
                products = Product.objects.filter(user_id=id).order_by('-created_at')
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={
                    'message': 'Products not found'
                })
            
            serializer = ProductSerializer(products, many=True)
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
    

   
    
        
    
