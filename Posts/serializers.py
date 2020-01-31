from rest_framework import serializers
from Posts.models import AnimeModel, GenreModel


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreModel
        fields = ('title',)


class AnimeSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, source='title')

    class Meta:
        model = AnimeModel
        fields = ['title', 'description', 'image', 'studio', 'translate', 'sound', 'author', 'director', 'date', 'episodes', 'genre', 'country', 'year']



