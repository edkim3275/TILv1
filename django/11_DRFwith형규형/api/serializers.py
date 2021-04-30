from rest_framework import serializers
from .models import Artist, Music

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist')


class MusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title',)


class ArtistSerializer(serializers.ModelSerializer):
    musics = MusicSerializer(many=True)
    music_count = serializers.IntegerField(source='musics.count')
    class Meta:
        model = Artist
        fields = ('id', 'name', 'musics', 'music_count')
        read_only_fieids =('musics',)

class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', )