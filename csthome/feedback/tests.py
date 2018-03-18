from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Feedback


class FeedbackTests(APITestCase):
    """Test suite for the feedback model."""

    def test_send_feedback(self):
        """Ensure we can send a feedback to the server."""
        url = reverse('feedback:send-feedback')
        data = {'body': 'This is a test.'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feedback.objects.count(), 1)
