from django.shortcuts import render, redirect
from .forms import UserRegForm, EditProfileForm, ProfileImageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, f'User {first_name} {last_name} created!')
            return redirect('profile')
    else:
        form = UserRegForm()

    context = {
        'form': form,
    }
    return render(request, 'users/registration.html', context=context)


@login_required
def profile(request):
    if request.method == 'POST':
        edit_profile_form = EditProfileForm(request.POST, instance=request.user)
        profile_image_form = ProfileImageForm(request.POST, request.FILES, instance=request.user)

        if edit_profile_form.is_valid() and profile_image_form.is_valid():
            edit_profile_form.save()
            profile_image_form.save()
            messages.success(request, f'Your profile has been successfully updated')
            return redirect('profile')

    else:
        edit_profile_form = EditProfileForm(instance=request.user)
        profile_image_form = ProfileImageForm(instance=request.user)

    context = {
        'edit_profile_form': edit_profile_form,
        'profile_image_form': profile_image_form,
    }
    return render(request, 'users/profile.html', context=context)
