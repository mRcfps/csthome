from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import UserSerializer, ProfileSerializer


class UserLoginView(APIView):
    """When login for the first time, a token for the user will be
    created and stored."""

    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class UserChangePasswordView(generics.UpdateAPIView):
    """Allow users to change their password with token auth."""

    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)

    def get_object(self):
        return User.objects.get(id=self.request.user.id)


class UserProfileView(generics.RetrieveUpdateAPIView):
    """Allow users to retrieve or update their profile."""

    parser_classes = (MultiPartParser,)
    serializer_class = ProfileSerializer
    authentication_classes = (TokenAuthentication,)

    def get_object(self):
        profile = Profile.objects.get_or_create(user=self.request.user)
        return self.request.user.profile
