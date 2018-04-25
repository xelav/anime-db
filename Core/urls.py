from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from Anime import views
from django.conf.urls import url
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

url_router = routers.SimpleRouter()

url_router.register(r'anime', views.AnimeViewSet, base_name='anime')
url_router.register(r'episodes', views.EpisodeViewSet)
url_router.register(r'characters', views.CharacterViewSet, base_name='characters')
# url_router.register(r'producer', views.ProducerViewSet)

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
    url(r'^anime-seasons/(?P<year>[0-9]+)/$', views.get_yearly_anime_count),
    url(r'^category-count/$', views.get_category_count),
    url(r'^producer-count/$', views.get_producer_count),

    # url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += url_router.urls
