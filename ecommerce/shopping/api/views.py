from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from shopping.models import Shopping_List, Shopping_List_Item
from shopping.api.serializers import ShoppingListSerializer
from rest_framework.permissions import IsAuthenticated

class ShoppingListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        shopping_list = Shopping_List.objects.filter(user=request.user.id)[0]
        print(shopping_list)
        serializer = ShoppingListSerializer(data=shopping_list)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)