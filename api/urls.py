from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, RegionViewSet, CartViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'carts', CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
