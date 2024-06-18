from rest_framework import viewsets
from .models import Product, Category, Region, Cart
from .serializers import ProductSerializer, CategorySerializer, RegionSerializer, CartSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name', None)
        category = self.request.GET.get('category', None)
        region = self.request.GET.get('region', None)
        min_price = self.request.GET.get('min', None)
        max_price = self.request.GET.get('max', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        if category is not None:
            queryset = queryset.filter(category_id=category)
        if region is not None:
            queryset = queryset.filter(region_id=region)
        if min_price and max_price and float(min_price) < float(max_price):
            queryset = queryset.filter(price__range=(
                float(min_price), float(max_price)))
        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.GET.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset
