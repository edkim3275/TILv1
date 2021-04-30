from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Artist, Music
from .serializers import ArtistSerializer, ArtistListSerializer, MusicSerializer, MusicListSerializer


@api_view(['GET', 'POST'])
def artist_list_or_create(request):
    artists = Artist.objects.all()
    if request.method == 'GET':
        serializer = ArtistListSerializer(instance=artists, many=True)
    elif request.method == 'POST':
        pass

def artist_detail(request):
    pass

def music_create(request):
    pass

def music_list(request):
    pass

def music_detail_or_update_or_delete(request):
    pass