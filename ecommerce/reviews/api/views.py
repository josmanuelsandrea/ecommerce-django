from rest_framework.viewsets import ModelViewSet
from reviews.models import Review
from reviews.api.serializers import ReviewSerializer
from reviews.api.permissions import ReviewOwnerPrivilege

class ReviewModelViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [ReviewOwnerPrivilege]