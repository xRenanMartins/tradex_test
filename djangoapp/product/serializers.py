from rest_framework import serializers
from .models import Product, VariationPrice

class VariationPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariationPrice
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    price_variations = VariationPriceSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'