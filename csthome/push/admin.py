from django.contrib import admin
from django.shortcuts import reverse

from .models import PushNotification


def send_push_notification(obj):
    if obj.has_pushed:
        return '已成功推送'
    else:
        return '<a href="{}">推送消息</a>'.format(
            reverse('push:push-notification', args=[obj.id])
        )

send_push_notification.allow_tags = True


@admin.register(PushNotification)
class PushNotificationAdmin(admin.ModelAdmin):

    list_display = ('content', 'created', 'has_pushed', send_push_notification)
    list_filter = ('created', 'has_pushed')

    send_push_notification.short_description = ''
