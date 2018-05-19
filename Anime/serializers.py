from rest_framework import serializers
from .models import *


class AnimeSerializer(serializers.ModelSerializer):
    age_restriction = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='age_restriction'
    )
    start_date = serializers.DateTimeField(format="%Y-%m-%d", required=False, allow_null=True, input_formats=["%Y-%m-%d"])
    end_date = serializers.DateTimeField(format="%Y-%m-%d", required=False, allow_null=True, input_formats=["%Y-%m-%d"])

    class Meta:
        model = Anime
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at',)


class CharacterSerializer(serializers.ModelSerializer):

    anime_id = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=Anime.objects.all(),
        source='anime'
    )
    anime_name = serializers.SlugRelatedField(
        read_only=True,
        slug_field='canonical_title',
        source='anime'
    )

    class Meta:
        model = Character
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at',)


class EpisodeSerializer(serializers.ModelSerializer):
    anime_id = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=Anime.objects.all(),
        source='anime'
    )
    anime_name = serializers.SlugRelatedField(
        read_only=True,
        slug_field='canonical_title',
        source='anime'
    )
    air_date = serializers.DateTimeField(format="%Y-%m-%d", required=False, allow_null=True, input_formats=["%Y-%m-%d"])

    class Meta:
        model = Episode
        fields = '__all__'


class ProducerSerializer(serializers.ModelSerializer):
    anime_id = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=Anime.objects.all(),
        source='anime'
    )
    anime_name = serializers.SlugRelatedField(
        read_only=True,
        slug_field='canonical_title',
        source='anime'
    )

    class Meta:
        model = Producer
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at',)


class CategorySerializer(serializers.ModelSerializer):
    anime_id = serializers.IntegerField(
        required=True,
        # queryset=Anime.objects.all(),
        source='anime',
    )
    # anime_name = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='canonical_title',
    #     source='anime'
    # )

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at',)
