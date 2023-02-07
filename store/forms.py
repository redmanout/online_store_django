from django import forms
from .models import ReviewsProduct


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewsProduct
        fields = ('email', 'name', 'text',)
