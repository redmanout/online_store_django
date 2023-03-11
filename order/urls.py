from django.urls import path
from . import views

urlpatterns = [
    path('store/order/addtocart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('store/order/deletefromcart/<int:id>', views.delete_from_cart, name='delete_from_cart'),
    path('store/order/orderproduct/', views.order_product, name='order_product'),
]
