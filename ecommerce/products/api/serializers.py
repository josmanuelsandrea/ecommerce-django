from rest_framework.serializers import ModelSerializer
from products.models import Product
from users.api.serializers import UserInfoNeeded
from users.models import User
from categories.api.serializers import CategoriesSerializer
from categories.models import Category
from ecommerce.tools import RelatedFieldAlternative

class ProductSerializer(ModelSerializer):
    seller = RelatedFieldAlternative(queryset=User.objects.all(), serializer=UserInfoNeeded)
    category = RelatedFieldAlternative(queryset=Category.objects.all(), serializer=CategoriesSerializer)

    class Meta:
        model = Product
        fields = ['id', 'name', 'product_image', 'existence', 'category', 'seller', 'price']