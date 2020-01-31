from django.shortcuts import render
from rest_framework import viewsets
from Posts.models import AnimeModel, GenreModel
from Posts.serializers import AnimeSerializer, GenreSerializer
from rest_framework import generics, permissions


class AnimeViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AnimeSerializer
    queryset = AnimeModel.objects.all()


class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GenreSerializer
    queryset = GenreModel.objects.all()
