from rest_framework import serializers
from .models import *


class AnimeSerializer(serializers.ModelSerializer):
    age_restriction = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='age_restriction'
    )

    class Meta:
        model = Anime
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):

    anime = AnimeSerializer(read_only=True)

    class Meta:
        model = Character
        fields = '__all__'


class EpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Episode
        fields = '__all__'


class ProducerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producer
        fields = '__all__'
