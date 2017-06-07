from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Event, News
from .serializers import (EventListSerializer,
                          EventDetailSerializer,
                          NewsListSerializer,
                          NewsDetailSerializer)


def welcome(request):
    return HttpResponse("Welcome to CST Home!")


class EventListView(generics.ListAPIView):
    """A view that lists all events."""

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
    """A view that display detailed info of an event."""

    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

    def get_object(self):
        return Event.objects.get(id=self.kwargs['pk'])


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
    """A view that lists all news."""

    queryset = News.objects.all()
    serializer_class = NewsListSerializer


class NewsDetailView(generics.RetrieveAPIView):
    """A view that display detailed info of an event."""

    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer

    def get_object(self):
        return News.objects.get(id=self.kwargs['pk'])


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
