from django.urls import path
from shopping.api.views import ShoppingListAPIView, ShoppingListItemAPIView

urlpatterns = [
    path('shopping_list/list', ShoppingListAPIView.as_view(), name='Shopping_List_Retrieve'),
    path('shopping_list/add_item', ShoppingListItemAPIView.as_view(), name='Shopping_List_Items')
]