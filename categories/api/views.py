from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsStaffOrReadOnly

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(published=True)
    lookup_field = 'slug'





