from rest_framework import serializers
from .models import Supplier, Product, Merchandizer

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class MerchandizerSerializer(serializers.ModelSerializer):
    products_managed = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Merchandizer
        fields = '__all__'
