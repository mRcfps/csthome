from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings

from .models import Event, News

# Number of news for test
# Should be larger than PAGE_SIZE
TEST_NEWS_NUM = 20

# Number of events for test
# Should be larger than PAGE_SIZE
TEST_ACTIVE_EVENTS_NUM = 20

# Number of events to display in carousel
TEST_HEADLINE_EVENTS_NUM = 5


class NewsTests(APITestCase):
    """Test suite for the news model."""

    def setUp(self):
        """Add some events to play with."""
        for _ in range(TEST_NEWS_NUM):
            news = News(title='Test News', body='This is a test news.')
            news.save()

        self.test_news = News.objects.all()[0]

    def test_get_news_list(self):
        """Ensure we can get a list of news."""
        url = reverse('home:news-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], TEST_NEWS_NUM)

        # Check if the num of news is equal to PAGE SIZE in settings
        self.assertEqual(len(response.data['results']), api_settings.PAGE_SIZE)

        # Check if the response has `next` field
        self.assertNotEqual(response.data['next'], None)

    def test_get_news_by_id(self):
        """Ensure we can get news by its id."""
        url = reverse('home:news-detail', kwargs={'pk': self.test_news.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.test_news.id)


class EventTests(APITestCase):
    """Test suite for the event model."""

    def setUp(self):
        """Add some events to play with."""

        # Add some active events
        for _ in range(TEST_ACTIVE_EVENTS_NUM):
            event = Event(title='Active Event',
                          body='This is a test active event.',
                          is_active=True)
            event.save()

        # Add some headline events
        for _ in range(TEST_HEADLINE_EVENTS_NUM):
            event = Event(title='Headline Event',
                          body='This is a test headline event.',
                          is_headline=True)
            event.save()

        self.test_event = Event.objects.all()[0]

    def test_get_headline_events(self):
        """Ensure we can get all headline news."""

        url = reverse('home:event-list') + '?headline=true'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], TEST_HEADLINE_EVENTS_NUM)

    def test_get_active_events(self):
        """Ensure we can get all active news."""

        url = reverse('home:event-list') + '?active=true'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), api_settings.PAGE_SIZE)

    def test_get_event_by_id(self):
        """Ensure we can get news by its id."""

        url = reverse('home:event-detail', kwargs={'pk': self.test_event.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.test_event.id)

    def test_attend_event(self):
        """Ensure we can attend the event by `GET` this endpoint."""

        user = User.objects.create(username='test', password='testismylife')
        client = APIClient()
        client.force_authenticate(user=user)
        url = reverse('home:attend-event', kwargs={'pk': self.test_event.id})
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the user is contained in test event's attendees
        self.assertEqual(self.test_event.attendees.count(), 1)
