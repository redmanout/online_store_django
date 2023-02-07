from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryList.as_view(), name='main_page'),
    path('store/product/<slug>', views.ProductDetailView.as_view(), name='product'),
    path('store/about/', views.about_us, name='about'),
    path('store/shipping-and-payment/', views.ship_pay, name='ship_pay'),
    path('store/contacts/', views.contacts, name='contacts'),
    path('review/<int:pk>/', views.ProductDetailView.as_view(), name='add_review'),
]
