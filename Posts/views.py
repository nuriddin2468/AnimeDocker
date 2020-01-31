from django.shortcuts import render
from rest_framework import viewsets
from Anime.models import AnimeModel, GenreModel
from Anime.serializers import AnimeSerializer, GenreSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication



class AnimeViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AnimeSerializer
    queryset = AnimeModel.objects.all()


class GenreViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = GenreSerializer
    queryset = GenreModel.objects.all()
