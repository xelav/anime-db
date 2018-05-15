from django.conf.urls import url
from .app_views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^main-menu/$', main_menu, name='main-menu'),

]

urlpatterns = format_suffix_patterns(urlpatterns)