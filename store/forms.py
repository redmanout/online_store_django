from django import forms
from store.models import ReviewsProduct


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewsProduct
        fields = ('email', 'name', 'text',)
