from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .models import Artist, Music
from serializers import ArtistListSerializer, ArtistSerializer, MusicSerializer, MusicListSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def artists_list_create(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistListSerializer(instance=artists, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            Response(status=status.HTTP_400_BAD_REQUEST)