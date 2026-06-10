
from django.urls import path
from . import views

app_name = 'pastry'

urlpatterns = [
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),  # ← ПЕРВЫМ!
    path('', views.ProductListView.as_view(), name='product_list'),
    path('category/<slug:slug>/', views.ProductListByCategoryView.as_view(), name='product_list_by_category'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]