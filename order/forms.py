from django import forms
from .models import StoreCart, Order


class StoreCartForm(forms.ModelForm):
    class Meta:
        model = StoreCart
        fields = ('quantity',)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'phone', 'address', 'city', 'country',)