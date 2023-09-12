from rest_framework.serializers import ModelSerializer
from products.models import Product
from users.api.serializers import UserInfoNeeded
from categories.api.serializers import CategoriesSerializer

class ProductSerializer(ModelSerializer):
    seller = UserInfoNeeded()
    category = CategoriesSerializer()
    class Meta:
        model = Product
        fields = ['id', 'name', 'product_image', 'existence', 'category', 'seller', 'price']
        read_only_fields = ['seller']
    
    def create(self, validated_data):
        user = self.context['request'].user

        validated_data['seller'] = user

        product = Product.objects.create(**validated_data)
        return product