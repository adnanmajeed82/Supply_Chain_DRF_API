from django.urls import path
from .views import SupplierList, SupplierDetail
from django.urls import path
from .views import ProductList, ProductDetail
from .views import MerchandizerList, MerchandizerDetail

urlpatterns = [
    path('suppliers/', SupplierList.as_view(), name='supplier-list'),
    path('suppliers/<int:pk>/', SupplierDetail.as_view(), name='supplier-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('merchandizers/', MerchandizerList.as_view(), name='merchandizer-list'),
    path('merchandizers/<int:pk>/', MerchandizerDetail.as_view(), name='merchandizer-detail'),
]



 



 
