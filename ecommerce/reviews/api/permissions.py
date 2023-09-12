from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from reviews.models import Review

class ReviewOwnerPrivilege(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        if request.method == 'POST':
            if request.user.is_anonymous is False:
                return True
            self.message = "You are not logged in"
            return False

        else:
            id_review = view.kwargs.get('pk')
            review = get_object_or_404(Review, pk=id_review)
            id_user = request.user.pk
            id_user_product = review.seller.pk

            if id_user == id_user_product:
                return True

            self.message = "You are not the author of this review."
            return False