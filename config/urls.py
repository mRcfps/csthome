from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework.documentation import include_docs_urls

from home.views import welcome


urlpatterns = [
    path('home/', include('home.urls')),
    path('users/', include('users.urls')),
    path('feedback/', include('feedback.urls')),
    path('push/', include('push.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='CSTHome API')),
    path('', welcome),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
