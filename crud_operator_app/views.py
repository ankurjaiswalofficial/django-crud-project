from rest_framework import viewsets, filters
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from django.utils.dateparse import parse_date

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        created_at = self.request.query_params.get('created_at', None)
        if created_at:
            date_obj = parse_date(created_at)
            print(created_at, date_obj)
            if date_obj:
                queryset = queryset.filter(created_at__date=date_obj)
        return queryset


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        created_at = self.request.query_params.get('created_at', None)
        if created_at:
            date_obj = parse_date(created_at)
            if date_obj:
                queryset = queryset.filter(created_at__date=date_obj)
        return queryset
