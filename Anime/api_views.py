from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from .serializers import *
from datetime import datetime


class AnimeViewSet(viewsets.ModelViewSet):
    """
    asdf
    
    list:qq
    
    create:asdq
    """

    pagination_class = LimitOffsetPagination
    serializer_class = AnimeSerializer

    def get_queryset(self):

        queryset = Anime.objects.all()

        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(canonical_title=title)

        return queryset


class CharacterViewSet(viewsets.ModelViewSet):

    pagination_class = LimitOffsetPagination
    serializer_class = CharacterSerializer

    def get_queryset(self):

        queryset = Character.objects.all()

        anime_title = self.request.query_params.get('anime_title')
        if anime_title:
            queryset = queryset.filter(anime__canonical_title=anime_title)

        character_name = self.request.query_params.get('character_name')
        if anime_title:
            queryset = queryset.filter(name=character_name)

        return queryset


class EpisodeViewSet(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination
    serializer_class = EpisodeSerializer

    queryset = Episode.objects.all()


class ProducerViewSet(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination
    serializer_class = EpisodeSerializer

    queryset = Producer.objects.all()


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

    category_title = request.query_params.get('category_title')

    query = Category.objects.filter(title=category_title)

    return Response({'count':query.count()})


@api_view(['GET'])
def get_producer_count(request):

    producer_name = request.query_params.get('producer_name')

    query = Producer.objects.filter(name=producer_name)

    return Response({'count':query.count()})