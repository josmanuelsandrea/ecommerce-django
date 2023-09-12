from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializers import CategoriesSerializer
from ecommerce.permissions import IsAdminOrReadOnly

class CategoriesModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [IsAdminOrReadOnly]