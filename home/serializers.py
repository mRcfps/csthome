from rest_framework import serializers

from .models import Event, News


class EventListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'title', 'photo', 'created',
                  'is_active', 'attendees')


class EventDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'title', 'photo', 'body', 'created')


class NewsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'title', 'photo', 'created')


class NewsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'
