from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from music.models import Music
from music.serializers import MusicSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = MusicSerializer








# Create your views here.
