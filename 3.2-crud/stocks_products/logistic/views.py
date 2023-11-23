from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['address']

    def get_queryset(self):
        queryset = Stock.objects.all()
        product_id = self.request.query_params.get('products', None)
        if product_id:
            queryset = queryset.filter(positions__product_id=product_id)
        return queryset
