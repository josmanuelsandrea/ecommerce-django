from rest_framework.serializers import ModelSerializer
from shopping.models import Shopping_List, Shopping_List_Item
from products.api.serializers import ProductSerializer
from ecommerce.tools import RelatedFieldAlternative
from products.models import Product

class ShoppingListSerializer(ModelSerializer):
    class Meta:
        model = Shopping_List
        fields = ['user', 'created_at', 'uuid']

class ReceiveShoppingListWithItemsSerializer(ModelSerializer):
    product = ProductSerializer()
    list_id = ShoppingListSerializer()
    class Meta:
        model = Shopping_List_Item
        fields = ['product', 'list_id', 'quantity']


class ShoppingListItemSerializer(ModelSerializer):
    product = RelatedFieldAlternative(queryset=Product.objects.all(), serializer=ProductSerializer)
    list_id = RelatedFieldAlternative(queryset=Shopping_List.objects.all(), serializer=ShoppingListSerializer)

    class Meta:
        model = Shopping_List_Item
        fields = ['product', 'list_id', 'quantity']
        read_only_fields = ['list_id']