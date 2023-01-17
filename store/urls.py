from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='main_page'),
    path('store/about/', views.about_us, name='about'),
    path('store/shipping-and-payment/', views.ship_pay, name='ship_pay'),
    path('store/contacts/', views.contacts, name='contacts'),
]
