from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .models import Movie
from .serializers import MovieSerializer, MovieListSerializer

@api_view(['GET', 'POST'])
def movie_index_or_create(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
         serializer = MovieSerializer(data=request.data)
         if serializer.is_valid(raise_exception=True):
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_or_update_or_delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie, read_only=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        movie.delete()
        data = {
            'message': '삭제완료'
        }
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)