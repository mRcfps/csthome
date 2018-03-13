from django.urls import path

from . import views

urlpatterns = [
    path(
        'push-notifications/<int:push_id>/$',
        views.admin_send_push_notifications,
        name='push-notification'),
]
