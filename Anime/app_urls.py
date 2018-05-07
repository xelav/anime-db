from django.conf.urls import url
from .app_views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^main-menu/$', main_menu, name='main-menu'),
    url(r'^search-anime/$', search_anime, name='search-anime'),
    url(r'^search-character/$', search_character, name='search-character'),

    url(r'^create-anime/$', create_anime),
    url(r'^create-character/$', create_character),
    url(r'^create-episode/$', create_episode),
    url(r'^create-producer/$', create_producer),

    url(r'^category-count/$', get_categories_count, name='category-count'),
    url(r'^producer-count/$', get_producers_count, name='producer-count'),

]

urlpatterns = format_suffix_patterns(urlpatterns)