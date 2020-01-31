from rest_framework import serializers
from Posts.models import AnimeModel, GenreModel


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreModel
        fields = ('title',)


class AnimeSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)

    class Meta:
        model = AnimeModel
        fields = ["__all__"]



