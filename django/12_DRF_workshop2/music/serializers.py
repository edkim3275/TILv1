from rest_framework import serializers
from .models import Artist, Music


class MusicListSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=2, max_length=20)
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist',)


class MusicSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=2, max_length=20)
    class Meta:
        model = Music 
        fields = '__all__'
        read_only_fields = ('artist',)


class ArtistListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=2, max_length=20)
    class Meta:
        model = Artist
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=2, max_length=20)
    music_set = MusicSerializer(many=True, read_only=True)
    music_count = serializers.IntegerField(source='music.count', read_only=True)
    class Meta:
        model = Artist
        fields = ('id', 'name', 'music_set', 'music_count',)