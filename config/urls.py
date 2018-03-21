from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

from home.views import welcome


urlpatterns = [
    path('home/', include('home.urls', namespace='home')),
    path('users/', include('users.urls', namespace='users')),
    path('feedback/', include('feedback.urls', namespace='feedback')),
    path('push/', include('push.urls', namespace='push')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', welcome),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
