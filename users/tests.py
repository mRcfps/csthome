from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from .models import Profile


class UserTests(APITestCase):
    """Test suite for the user model."""

    def setUp(self):
        """Initialize a user to play with."""
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', password='test')

    def test_login(self):
        """Ensure we can login and get a token."""
        url = reverse('users:login')
        data = {'username': 'test', 'password': 'test'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['token'], None)

    def test_block_unregistered_user(self):
        """Ensure an unregistered user cannot login."""
        url = reverse('users:login')
        data = {'username': 'bad guy', 'password': 'reallybad'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_with_wrong_password(self):
        """Ensure we cannot login when password is wrong."""
        url = reverse('users:login')
        data = {'username': 'test', 'password': 'wrong'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_change_password(self):
        """Ensure we can change password."""
        url = reverse('users:change-password')
        data = {'username': 'test', 'password': 'newpassword'}
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Then let's login with the new password
        url = reverse('users:login')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfileTests(APITestCase):
    """Test suite for the profile model."""

    def setUp(self):
        """Initialize a user to play with."""
        self.user = User.objects.create_user(username='test', password='test')
        self.client = APIClient()

    def test_get_profile(self):
        """Ensure we can get profile of the user."""
        url = reverse('users:profile')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_profile(self):
        """Ensure we can update user's profile."""
        url = reverse('users:profile')
        data = {'full_name': 'Test Test'}
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user.profile.full_name, data['full_name'])
