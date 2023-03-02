from django import forms
from .models import StoreCart


class StoreCartForm(forms.ModelForm):
    class Meta:
        model = StoreCart
        fields = ('quantity',)
