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
        'notes/',
        views.NoteListView.as_view(),
        name='note-list'
    ),
    path(
        'notes/<int:pk>/',
        views.NoteDetailView.as_view(),
        name='note-detail'
    ),
    path(
        'admin/event/<int:event_id>/',
        views.admin_event_attendance,
        name='admin-event-attendance'
    )
]
