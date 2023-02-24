from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryList.as_view(), name='main_page'),
    path('store/search/', views.SearchView.as_view(), name='search'),
    path('store/products/', views.CatalogFilter.as_view(), name='catalog'),
    path('store/product/<slug>', views.ProductDetailView.as_view(), name='product'),
    path('review/<int:pk>/', views.ProductDetailView.as_view(), name='add_review'),
]
