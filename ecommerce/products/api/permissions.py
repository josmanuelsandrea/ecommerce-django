from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from products.models import Product

class ProductOwnerPrivilege(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        if request.method == 'POST':
            if request.user.is_anonymous is False:
                return True
            self.message = "You are not logged in"
            return False

        else:
            id_product = view.kwargs.get('pk')
            product = get_object_or_404(Product, pk=id_product)
            id_user = request.user.pk
            id_user_product = product.seller.pk

            if id_user == id_user_product:
                return True

            self.message = "You are not the seller of the product, you cannot alter the information or delete this product"
            return False