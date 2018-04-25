from rest_framework import serializers
from .models import *


class AnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anime
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):

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
