from rest_framework import serializers
from Posts.models import AnimeModel, GenreModel


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreModel
        fields = ('title',)


class AnimeSerializer(serializers.ModelSerializer):
    genre_test = GenreSerializer(many=True, read_only=False, source='genre')

    class Meta:
        model = AnimeModel
        fields = ['title', 'description', 'image', 'studio', 'translate', 'sound', 'author', 'director', 'date', 'episodes', 'genre_test', 'country', 'year']



