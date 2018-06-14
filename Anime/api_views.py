from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from django.db.models import Count

from .serializers import *
import datetime


class AnimeViewSet(viewsets.ModelViewSet):

    pagination_class = LimitOffsetPagination
    serializer_class = AnimeSerializer

    def get_queryset(self):

        queryset = Anime.objects.all().order_by('canonical_title')

        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(canonical_title__contains=title)

        return queryset


class CharacterViewSet(viewsets.ModelViewSet):

    pagination_class = LimitOffsetPagination
    serializer_class = CharacterSerializer

    def get_queryset(self):

        queryset = Character.objects.all().order_by('name')

        anime_title = self.request.query_params.get('anime_title')
        if anime_title:
            queryset = queryset.filter(anime__canonical_title=anime_title)

        character_name = self.request.query_params.get('character_name')
        if character_name:
            queryset = queryset.filter(name=character_name)

        return queryset


class EpisodeViewSet(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination
    serializer_class = EpisodeSerializer

    queryset = Episode.objects.all().order_by('canonical_title')


class ProducerViewSet(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination
    serializer_class = ProducerSerializer

    queryset = Producer.objects.all().order_by('name')


class CategoryViewSet(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination
    serializer_class = CategorySerializer

    queryset = Category.objects.all().order_by('title')


@api_view(['GET'])
def get_yearly_anime_count(request, year, format=None):

    year = int(year)
    winter = Anime.objects.filter(start_date__gte=datetime(year-1, 12, 1)).filter(start_date__lte=datetime(year, 2, 28))
    spring = Anime.objects.filter(start_date__gte=datetime(year, 3, 1)).filter(start_date__lte=datetime(year, 5, 31))
    summer = Anime.objects.filter(start_date__gte=datetime(year, 6, 1)).filter(start_date__lte=datetime(year, 8, 31))
    autumn = Anime.objects.filter(start_date__gte=datetime(year, 9, 1)).filter(start_date__lte=datetime(year, 11, 30))

    d = {'winter': winter.count(),
         'spring': spring.count(),
         'summer': summer.count(),
         'autumn': autumn.count()
         }

    return Response(d)


@api_view(['GET'])
def get_category_count(request):

    # category_title = request.query_params.get('category_title')

    query = Category.objects.values('title').annotate(count=Count('title'))

    return Response(query)


@api_view(['GET'])
def get_producer_count(request):

    # producer_name = request.query_params.get('producer_name')

    query = Producer.objects.values('name').annotate(count=Count('name'))

    return Response(query)
