from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from home.views import welcome

urlpatterns = [
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^feedback/', include('feedback.urls', namespace='feedback')),
    url(r'^push/', include('push.urls', namespace='push')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', welcome),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
