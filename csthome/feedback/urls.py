from django.urls import path

from . import views

urlpatterns = [
    path('', views.FeedbackCreateView.as_view(), name='send-feedback'),
]
