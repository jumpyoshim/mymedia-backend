"""
mymedia URL Configuration
"""
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from django.contrib import admin
from django.urls import include, path, re_path

schema_view = get_schema_view(
   openapi.Info(
      title='mymedia API',
      default_version='v1',
      description='SSKDs for mymedia project.',
      terms_of_service='https://www.google.com/policies/terms/',
      contact=openapi.Contact(email='jumpyoshim@gmail.com'),
      license=openapi.License(name='MIT License'),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('users/', include('users.urls')),
    path('groups/', include('groups.urls')),
]
