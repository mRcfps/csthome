from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.html import format_html

from rest_framework.authtoken.models import Token

from .models import Event, News


def view_attendance(obj):
    if obj.is_active:
        return format_html(
            '<a href="{}">查看签到情况</a>',
            reverse('home:admin-event-attendance', args=[obj.id])
        )
    else:
        # the event is not active
        return None


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = ('title', 'created', 'is_active',
                    'is_headline', view_attendance)
    search_fields = ('title',)
    date_hierarchy = 'created'
    list_filter = ('created', 'is_active', 'is_headline')
    list_editable = ('is_headline',)

    view_attendance.short_description = ''


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = ('title', 'created')
    list_filter = ('created',)
    search_fields = ('title',)


admin.site.site_header = 'CST党员之家'
admin.site.site_title = '后台管理'
admin.site.site_url = None

# Unregister default apps
admin.site.unregister(Group)
admin.site.unregister(Token)
