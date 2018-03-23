from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

from csthome.home.views import welcome

urlpatterns = [
    path('home/', include('csthome.home.urls', namespace='home')),
    path('users/', include('csthome.users.urls', namespace='users')),
    path('feedback/', include('csthome.feedback.urls', namespace='feedback')),
    path('push/', include('csthome.push.urls', namespace='push')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', welcome),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
