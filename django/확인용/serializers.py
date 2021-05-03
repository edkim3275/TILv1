from rest_framework import serializers
from .models import Artist, Music


# 모든 음악 정보 반환 
class MusicListSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    
    class Meta:
        model = Music 
        fields = ('id', 'title', )
        # read_only_fields = ('artist', )


# 상세 음악 정보 반환 
class MusicSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    # artist = serializers.CharField(max_length=30)  # 이거 foreignkey.. 
    # artist_name = serializers.CharField(max_length=30, source='artist.name')
    
    class Meta: 
        model = Music
        fields = '__all__'
        read_only_fields = ('artist',)  # 음악 업데이트 할 때, artist 정보는 바뀌지 않도록 ㅇㅎ! 
        # 업데이트 할 때 이거 안 해놓으면 에러나옴 


# 모든 가수의 정보 반환 
class ArtistListSerializer(serializers.ModelSerializer): 
    name = serializers.CharField(max_length=30)

    class Meta: 
        model = Artist
        fields = '__all__'


# 상세 가수 정보 생성 및 반환 
class ArtistSerializer(serializers.ModelSerializer): 
    name = serializers.CharField(max_length=30)
    music_set = MusicSerializer(many=True, read_only=True)
    # 새로운 값을 생성 
    music_count = serializers.IntegerField(source='music_set.count', read_only=True)
    
    class Meta: 
        model = Artist
        fields = ('id', 'name', 'music_set', 'music_count', )
