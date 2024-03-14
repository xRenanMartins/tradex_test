from django.urls import path
from product.views import ProductListCreateView, ProductRetrieveUpdateDestroyAPIView

app_name = 'product'

urlpatterns = [
    path('products', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
]