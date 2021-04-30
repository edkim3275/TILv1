from rest_framework import serializers
from .models import Artist, Music


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title')


class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name',)


class ArtistSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True, read_only=True)
    music_count = serializers.IntegerField(source='music.count')
    class Meta:
        model = Artist
        fields = ('id', 'name', 'music_set', 'music_count',)


class MusicListSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=2, max_length=20)
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist',)
