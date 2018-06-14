from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include

from django.views.generic.base import RedirectView

urlpatterns = [

    path('admin/', admin.site.urls),

    url(r'^api/', include('Anime.api_urls')),
    url(r'^app/', include('Anime.app_urls')),

    url(r'^.*$', RedirectView.as_view(pattern_name='main-menu', permanent=False), name='index')
]

# urlpatterns = format_suffix_patterns(urlpatterns)
