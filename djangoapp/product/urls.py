from django.urls import path
from product.views import ProductListCreateView, ProductDetailView, VariationPriceListCreateView, VariationPriceDetailView

app_name = 'product'

urlpatterns = [
    path('products', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('variations', VariationPriceListCreateView.as_view(), name='variation-list-create'),
    path('variations/<int:pk>', VariationPriceDetailView.as_view(), name='variation-detail'),
]