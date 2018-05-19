from django.conf.urls import url
from .api_views import *
from rest_framework import routers
from .api_views import *
from rest_framework.urlpatterns import format_suffix_patterns

url_router = routers.SimpleRouter()

url_router.register(r'anime', AnimeViewSet, base_name='anime')
url_router.register(r'episodes', EpisodeViewSet, base_name='episodes')
url_router.register(r'characters', CharacterViewSet, base_name='characters')
url_router.register(r'producers', ProducerViewSet, base_name='producers')
url_router.register(r'categories', CategoryViewSet, base_name='categories')

urlpatterns = [

    url(r'^anime-seasons/(?P<year>[0-9]+)/$', get_yearly_anime_count),
    url(r'^category-count/$', get_category_count),
    url(r'^producer-count/$', get_producer_count),

]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += url_router.urls