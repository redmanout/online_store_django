from django.contrib.auth.forms import UserCreationForm
from django import forms


from .models import CustomUser


class UserRegForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input_reg_form', 'placeholder': 'Enter your first name'}),
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input_reg_form', 'placeholder': 'Enter your last name'}),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input_reg_form', 'placeholder': 'Enter your email'}),
    )
    password1 = forms.CharField(
        label='Enter the password',
        widget=forms.PasswordInput(attrs={'class': 'input_reg_form', 'placeholder': 'Enter password'}),
    )
    password2 = forms.CharField(
        label='Confirm the password',
        widget=forms.PasswordInput(attrs={'class': 'input_reg_form', 'placeholder': 'Confirm password'}),
    )

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )


class EditProfileForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input_reg_form', 'placeholder': 'Enter your email'}),
    )

    class Meta:
        model = CustomUser
        fields = (
            'email',
        )


class ProfileImageForm(forms.ModelForm):
    avatar = forms.ImageField(
        required=False,
        label='Upload a photo',
        widget=forms.FileInput,
    )

    class Meta:
        model = CustomUser
        fields = ('avatar',)
