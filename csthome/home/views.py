from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Event, News, Note
from .serializers import (
    EventDetailSerializer,
    EventListSerializer,
    NewsDetailSerializer,
    NewsListSerializer,
    NoteListSerializer,
    NoteDetailSerializer,
)


def welcome(request):
    return HttpResponse("Welcome to CST Home!")


class EventListView(generics.ListAPIView):
    """Lists all events with page-number pagination."""

    serializer_class = EventListSerializer

    def get_queryset(self):
        """If `active` or `headline` query parameters is given,
        return all the qualified events.
        """
        queryset = Event.objects.all()
        is_active = self.request.query_params.get('active', False)
        is_headline = self.request.query_params.get('headline', False)

        if is_active:
            queryset = queryset.filter(is_active=True)

        if is_headline:
            queryset = queryset.filter(is_headline=True)

        return queryset


class EventDetailView(generics.RetrieveAPIView):
    """Retrieve one single event by id."""

    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer


class AttendEventView(APIView):
    """`GET` this view and the user of this request will be added to
    attendees of the event.
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        event = Event.objects.get(id=self.kwargs['pk'])
        event.attendees.add(self.request.user)
        event.save()

        return Response({'has_attended': True})


class NewsListView(generics.ListAPIView):
    """Lists all news with page-number pagination."""

    queryset = News.objects.all()
    serializer_class = NewsListSerializer


class NewsDetailView(generics.RetrieveAPIView):
    """Retrieve one single news by id."""

    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer


class NoteListView(generics.ListAPIView):
    """List all course notes."""

    queryset = Note.objects.all()
    serializer_class = NoteListSerializer
    pagination_class = None


class NoteDetailView(generics.RetrieveAPIView):
    """Retrieve one single note by id."""

    queryset = Note.objects.all()
    serializer_class = NoteDetailSerializer


@staff_member_required
def admin_event_attendance(request, event_id):
    """View attendees and absentees in admin."""

    event = get_object_or_404(Event, id=event_id)

    # get attendees and absentees of the given event
    # and pass them to the context
    attendees = event.attendees.all()
    absentees = set(User.objects.exclude(username='admin')) - set(attendees)
    context = {'event': event, 'attendees': attendees, 'absentees': absentees}

    return render(request, 'admin/home/event/detail.html', context)
