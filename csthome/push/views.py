import requests
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, render
from rest_framework import status

from .models import PushNotification

APP_ID     = '7U37shB86JaWjHwIWSvVV8wB-gzGzoHsz'
APP_KEY    = 'n5MyRip3G3NsBvNxSCX13ep8'
MASTER_KEY = 'O7MNG79CrA1I1hh0B5Rq4ONP'
PUSH_URL   = 'https://api.leancloud.cn/1.1/push'


@staff_member_required
def admin_send_push_notifications(request, push_id):
    """Send push notifications via admin with one click."""

    push = get_object_or_404(PushNotification, id=push_id)

    # Send requests to LeanCloud REST API for push notifications
    headers = {'X-LC-Id': APP_ID,
               'X-LC-Key': APP_KEY,
               'Content-Type': 'application/json'}
    response = requests.post(PUSH_URL,
                             json={'data': push.content},
                             headers=headers)

    if response.status_code == status.HTTP_200_OK:
        push.has_pushed = True
        push.save()

    return render(request, 'admin/push_result.html', {'push': push})
