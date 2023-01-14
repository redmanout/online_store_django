from django.urls import path
from django.contrib.auth import views as authViews
from . import views

urlpatterns = [
    path('store/user/register/', views.register, name='reg'),
    path('store/user/profile/', views.profile, name='profile'),
    path('store/user/login/', authViews.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('store/user/logout/', authViews.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('store/user/password-reset/', authViews.PasswordResetView.as_view(template_name='users/pass_reset.html'),
         name='pass_reset'),
    path('store/user/password_reset_confirm/<uidb64>/<token>/',
         authViews.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('store/user/password_reset_done/',
         authViews.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('store/user/password_reset_complete/',
         authViews.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]