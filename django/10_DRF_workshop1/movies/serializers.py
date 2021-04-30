from rest_framework import serializers
from .models import Movie

# 모든 게시물 정보 반환을 위한 Serializer
class MovieListSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=1, max_length=100)
    class Meta:
        model = Movie
        fields = ('id', 'title',)


# 상세 게시글 정보 반환을 위한 Serializer
class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=1, max_length=100)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'created_at', 'updated_at',)