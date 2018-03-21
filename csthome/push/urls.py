from django.urls import path

from . import views

app_name = 'push'

urlpatterns = [
    path(
        'push-notifications/<int:push_id>/',
        views.admin_send_push_notifications,
        name='push-notification'),
]
