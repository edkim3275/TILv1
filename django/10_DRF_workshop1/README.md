# workshop

- 순서정리하면서 DRF(Django Rest Framework)익히기

## 기초준비

```bash
# 가상환경 설정
$ python -m venv venv
$ source venv/Scripts/activate
$ touch .gitignore requirements.txt README.md
# 필요한 SW설치
$ pip install django django-extensions django-seed djangorestframework
$ django-admin startproject <pjt_name> .
# 설치된 내용 txt에 담아주기(for 협업)
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
```

- settings.py

  ```python
  INSTALLED_APPS = [
      'movies',
      'django_extensions',
      'django_seed',
      'rest_framework',
      ...
  ]
  ```

  - my_apps, 3rd party library .. 기입

- urls.py

  ```python
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/v1/', include('articles.urls')),
  ]
  ```

## models.py

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now_add : 생성 되었을 때만
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now : 계속해서 바뀌는 값
    updated_at = models.DateTimeField(auto_now=True)
```

## urls.py

1. article index / create : `GET / POST + api/v1/articles/`
2. article detail / update / delete : `GET / POST / DELETE + api/v1/articles/<int:article_pk>`

```python
from django.urls import path

urlpatterns = [
    path('articles/', views.article_index_or_create),
    path('articles/<int:article_pk>', views.article_detail_or_update_or_delete),
]
```

## migrations

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py seed <app_name> --number=int
```

## serializers.py

```python
from rest_framework import serializers
from .models import Movie

# 모든 게시물 정보 반환을 위한 Serializer
class MovieListSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=1, max_length=100)
    class Meta:
        model = Movie
        fields = ('title')

# 상세 게시글 정보 반환을 위한 Serializer
class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=1, max_length=100)
    # created_at = serializers.DateTimeField(auto_now_add=True)
    # updated_at = serializers.DateTimeField(auto_now=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'created_at', 'updated_at')
```

## views.py

```python
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
```

