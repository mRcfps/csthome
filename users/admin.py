from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user', 'full_name', 'sex',
        'identity', 'college', 'major'
    )
    list_filter = ('identity', 'college', 'major')
    search_fields = ('user', 'full_name')

admin.site.register(Profile, ProfileAdmin)
