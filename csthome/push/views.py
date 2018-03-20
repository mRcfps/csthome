from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, render
from rest_framework import status

from .models import PushNotification


@staff_member_required
def admin_send_push_notifications(request, push_id):
    """Send push notifications via admin with one click."""

    push = get_object_or_404(PushNotification, id=push_id)

    # Send requests to LeanCloud REST API for push notifications
    response = None

    if response.status_code == status.HTTP_200_OK:
        push.has_pushed = True
        push.save()

    return render(request, 'admin/push_result.html', {'push': push})
