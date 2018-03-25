from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):

    list_display = ('body', 'created')
    list_filter = ('created',)
