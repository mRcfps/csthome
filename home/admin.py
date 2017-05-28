from django.contrib import admin
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Event, News


def view_attendance(obj):
    if obj.is_active:
        return '<a href="{}">查看签到情况</a>'.format(
            reverse('home:admin-event-attendance', args=[obj.id])
        )
    else:
        # the event is not active
        return None

view_attendance.allow_tags = True


class EventAdmin(admin.ModelAdmin):

    list_display = ('title', 'created', 'is_active',
                    'is_headline', view_attendance)
    search_fields = ('title',)
    date_hierarchy = 'created'
    list_filter = ('created', 'is_active', 'is_headline')
    list_editable = ('is_headline',)

    view_attendance.short_description = ''


class NewsAdmin(admin.ModelAdmin):

    list_display = ('title', 'created')
    list_filter = ('created',)
    search_fields = ('title',)


admin.site.register(Event, EventAdmin)
admin.site.register(News, NewsAdmin)

admin.site.site_header = 'CST党员之家'
admin.site.site_title = '后台管理'
admin.site.site_url = None
