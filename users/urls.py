from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^login/$',
        views.UserLoginView.as_view(),
        name='login'
    ),
    url(
        r'^change-password/$',
        views.UserChangePasswordView.as_view(),
        name='change-password'
    ),
    url(
        r'^profile/$',
        views.UserProfileView.as_view(),
        name='profile'
    ),
]
