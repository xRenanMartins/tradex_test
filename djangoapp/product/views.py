from rest_framework import generics
from .models import Product, VariationPrice
from .serializers import ProductSerializer, VariationPriceSerializer
from rest_framework.response import Response

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class VariationPriceListCreateView(generics.ListCreateAPIView):
    queryset = VariationPrice.objects.all()
    serializer_class = VariationPriceSerializer

class VariationPriceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VariationPrice.objects.all()
    serializer_class = VariationPriceSerializer
