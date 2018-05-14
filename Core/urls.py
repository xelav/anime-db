from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.views.generic.base import RedirectView


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   validators=['flex', 'ssv'],
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('admin/', admin.site.urls),

    url(r'^api/', include('Anime.api_urls')),
    url(r'^app/', include('Anime.app_urls')),

    # url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),

    # url(r'^.*$', RedirectView.as_view(pattern_name='main-menu', permanent=False), name='index')
]

# urlpatterns = format_suffix_patterns(urlpatterns)
