from django.shortcuts import get_object_or_404
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Artist, Music
from .serializers import ArtistListSerializer, ArtistSerializer, MusicListSerializer, MusicSerializer

# Create your views here.

# api/v1/artists/
@api_view(['GET', 'POST'])
def artist_list_or_create(request): 
    if request.method == 'GET': 
        artists = Artist.objects.all()
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        

# api/v1/artists/<artist_pk>/
@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)


# api/v1/artists/<artist_pk>/music/
@api_view(['POST'])
def create_music(request, artist_pk): 
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True): 
        serializer.save(artist=artist)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


# api/v1/music/
@api_view(['GET'])
def music_list(request): 
    musics = Music.objects.all() 
    serializer = MusicListSerializer(musics, many=True)  
    # many=True 주의! 이거 없으니까 오류남ㅠㅠ
    return Response(serializer.data)


# api/v1/music/<music_pk>/
@api_view(['GET', 'PUT', 'DELETE'])
def music_detail_or_update_or_delete(request, music_pk): 
    music = get_object_or_404(Music, pk=music_pk)
    
    if request.method == 'GET': 
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    elif request.method == 'PUT': 
        serializer = MusicSerializer(instance=music, data=request.data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE': 
        data = {
            'id': music_pk
        }
        music.delete()
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)

