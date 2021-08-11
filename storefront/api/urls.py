from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, ProductImageViewSet, CategoryViewSet

router = DefaultRouter()

router.register('products',ProductViewSet, basename='product')
router.register('productimages',ProductImageViewSet, basename='productimage')
router.register('categories',CategoryViewSet, basename='category')

urlpatterns = router.urls