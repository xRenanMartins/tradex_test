from rest_framework import generics
from .models import Product, VariationPrice
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import date

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        price_min = float(serializer.validated_data.get('price_min'))
        price_max = float(serializer.validated_data.get('price_max'))
        new_price = price_max - price_min
        
        if new_price:
            VariationPrice.objects.create(product=instance, price=new_price)
        return Response(serializer.data)
