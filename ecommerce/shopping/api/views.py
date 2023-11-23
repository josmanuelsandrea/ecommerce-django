from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from shopping.models import Shopping_List, Shopping_List_Item
from shopping.api.serializers import ShoppingListSerializer, ShoppingListItemSerializer, ReceiveShoppingListWithItemsSerializer
from users.models import User
from drf_yasg.utils import swagger_auto_schema

class ShoppingListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    # RETRIEVE THE ITEMS OF THE SHOPPING LIST OF THE GIVEN USER
    @swagger_auto_schema(operation_description="Retrieve the items inside of the shopping list of the given user")
    def get(self, request):
        # Get the shopping list of an user
        shopping_list = Shopping_List.objects.filter(user=request.user.id)

        # If there is not existing shopping list for the user
        if (len(shopping_list) > 0):
            # Serialize the data
            ALL_ITEMS_INSIDE_LIST = Shopping_List_Item.objects.filter(list_id=shopping_list[0].id)
            serializer = ReceiveShoppingListWithItemsSerializer(instance=ALL_ITEMS_INSIDE_LIST, many=True)
            
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'detail': 'User does not have a shopping list'})
    
    @swagger_auto_schema(operation_description="Create a shopping list for the user")
    def post(self, request):
        # Check if there is an existing shopping list for the user
        shopping_list = Shopping_List.objects.filter(user=request.user.id)

        # If there is one (at least one) return the data of the current list
        if (len(shopping_list) > 0):
            serializer = ShoppingListSerializer(shopping_list, many=True)
            return Response(serializer.data)
        # In case there is not existing shopping_list, create one
        else:
            current_authenticated_user = User.objects.get(id=request.user.id)
            created_list = Shopping_List.objects.create(user=current_authenticated_user)
            serializer = ShoppingListSerializer(created_list)
            return Response(serializer.data)

class ShoppingListItemAPIView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(operation_description="Add an item to the shopping list of the given user")
    def post(self, request):
        CORRESPONDING_LIST = Shopping_List.objects.filter(user=request.user.id)[0]
        request.data._mutable = True
        request.data.update({"list_id": CORRESPONDING_LIST.id })
        serializer = ShoppingListItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data='Unexpected Error')