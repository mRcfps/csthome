from django.conf import settings
from django.urls import include, path
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from csthome.home.views import welcome

schema_view = get_schema_view(
    openapi.Info(
        title="CSTHome API",
        default_version="1.0.0",
        description="Server API For CSTHome APPs",
    ),
    public=True,
)

urlpatterns = [
    # API Documentation
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),

    path('home/', include('csthome.home.urls', namespace='home')),
    path('users/', include('csthome.users.urls', namespace='users')),
    path('feedback/', include('csthome.feedback.urls', namespace='feedback')),
    path('push/', include('csthome.push.urls', namespace='push')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', welcome),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
