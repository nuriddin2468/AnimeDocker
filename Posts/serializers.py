from rest_framework import serializers
from Posts.models import AnimeModel, GenreModel


class GenreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = GenreModel
        fields = ('id', 'title',)


class AnimeSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = AnimeModel
        fields = ['id', 'title', 'description', 'image', 'studio', 'translate', 'sound', 'author', 'director', 'date', 'episodes', 'genre', 'country', 'year']

    def create(self, validated_data):
        genres = validated_data.pop('genre')
        post = AnimeModel.objects.create(**validated_data)
        for genre in genres:
            try:
                x = GenreModel.objects.get(title=genre['title'])
                post.genre.add(x)
            except Exception:
                pass

        post.save()
        return post


