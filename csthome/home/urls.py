from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path(
        'events/',
        views.EventListView.as_view(),
        name='event-list'
    ),
    path(
        'events/<int:pk>/',
        views.EventDetailView.as_view(),
        name='event-detail'
    ),
    path(
        'events/<int:pk>/attend/',
        views.AttendEventView.as_view(),
        name='attend-event'
    ),
    path(
        'news/',
        views.NewsListView.as_view(),
        name='news-list'
    ),
    path(
        'news/<int:pk>/',
        views.NewsDetailView.as_view(),
        name='news-detail'
    ),
    path(
        'admin/event/<int:pk>/',
        views.admin_event_attendance,
        name='admin-event-attendance'
    )
]
