from rest_framework import viewsets
from .models import Supplier, Product, Merchandizer
from .serializers import SupplierSerializer, ProductSerializer, MerchandizerSerializer
from rest_framework import generics

 

class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MerchandizerList(generics.ListCreateAPIView):
    queryset = Merchandizer.objects.all()
    serializer_class = MerchandizerSerializer

class MerchandizerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Merchandizer.objects.all()
    serializer_class = MerchandizerSerializer

