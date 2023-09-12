from rest_framework.routers import DefaultRouter
from products.api.views import ProductModelViewSet

router_products = DefaultRouter()
router_products.register(prefix='products', basename='products', viewset=ProductModelViewSet)