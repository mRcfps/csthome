from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path(
        'login/',
        views.UserLoginView.as_view(),
        name='login'
    ),
    path(
        'change-password/',
        views.UserChangePasswordView.as_view(),
        name='change-password'
    ),
    path(
        'profile/',
        views.UserProfileView.as_view(),
        name='profile'
    ),
]
