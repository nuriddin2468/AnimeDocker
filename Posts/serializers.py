from rest_framework import serializers
from Posts.models import AnimeModel, GenreModel


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreModel
        fields = ('title',)


class AnimeSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    classification = serializers.ChoiceField(choices=AnimeModel.classification_choices)

    class Meta:
        model = AnimeModel
        fields = ('id', 'title', 'title_orig', 'text', 'date', 'info', 'image', 'genre', 'classification')



