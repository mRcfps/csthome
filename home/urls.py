from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    url(
        r'^events/$',
        views.EventListView.as_view(),
        name='event-list'
    ),
    url(
        r'^events/(?P<pk>\d+)/$',
        views.EventDetailView.as_view(),
        name='event-detail'
    ),
    url(
        r'^events/(?P<pk>\d+)/attend/$',
        views.AttendEventView.as_view(),
        name='attend-event'
    ),
    url(
        r'^news/$',
        views.NewsListView.as_view(),
        name='news-list'
    ),
    url(
        r'^news/(?P<pk>\d+)/$',
        views.NewsDetailView.as_view(),
        name='news-detail'
    ),
    url(
        r'admin/event/(?P<event_id>\d+)/$',
        views.admin_event_attendance,
        name='admin-event-attendance'
    )
]
