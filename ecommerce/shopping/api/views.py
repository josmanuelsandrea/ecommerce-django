from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from shopping.models import Shopping_List, Shopping_List_Item
from shopping.api.serializers import ShoppingListSerializer
from users.models import User


class ShoppingListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # Get the shopping list of an user
        shopping_list = Shopping_List.objects.filter(user=request.user.id)

        # If there is not existing shopping list for the user
        if (len(shopping_list) > 0):
            # Serialize the data
            serializer = ShoppingListSerializer(shopping_list, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'detail': 'User does not have a shopping list'})
    
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
        