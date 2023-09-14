from django.urls import path
from shopping.api.views import ShoppingListAPIView

urlpatterns = [
    path('shopping_list/retrieve', ShoppingListAPIView.as_view(), name='Shopping_List_Retrieve')
]