from rest_framework import serializers
from .models import Product, VariationPrice

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class VariationPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariationPrice
        fields = '__all__'