from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^push-notifications/(?P<push_id>\d+)/$',
        views.admin_send_push_noitifications,
        name='push-notification'),
]
