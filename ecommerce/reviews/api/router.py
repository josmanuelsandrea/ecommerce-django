from rest_framework.routers import DefaultRouter
from reviews.api.views import ReviewModelViewSet

router_reviews = DefaultRouter()
router_reviews.register(prefix='reviews', basename='reviews', viewset=ReviewModelViewSet)