from rest_framework.serializers import ModelSerializer
from shopping.models import Shopping_List

class ShoppingListSerializer(ModelSerializer):
    class Meta:
        model = Shopping_List
        fields = ['user', 'created_at', 'uuid']