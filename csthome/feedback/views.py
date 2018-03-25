from rest_framework import generics

from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackCreateView(generics.CreateAPIView):
    """Create a new feedback."""

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
