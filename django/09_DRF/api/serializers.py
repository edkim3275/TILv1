# serializers.py
from rest_framework import serializers
from .models import Article, Comment

# Serializer 의 존재이유
# 1. 데이터 검증
# 2. JSON 생성

# Comment 관련 JSON + validation 담당자
class CommentSerializer(serializers.ModelSerializer):
    content = serializers.CharField(min_length=1, max_length=200)
    class Meta:
        model = Comment
        # exclude = ('article', ) => validation / JSON 에서 모두 없는 취급
        # 쓰는 거에서 뺀다는 것 => 결국 항목에서 제외시킨다는 것
        fields = '__all__'  # JSON 에는 모든 필드가 포함 되고,
        read_only_fields = ('article',)  # CUD 관련 validation 은 포함 하지 않는다.
        

class ArticleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=2, max_length=100)
    content = serializers.CharField(min_length=2)
    
    # Comment 관련한 JSON도 포함해야 함 => CommentSerializer 가 들어 가야한다.
    # related_name 과 완전히 동일하게 작성
    comments = CommentSerializer(many=True, read_only=True)  # read_only 속성 == Meta 아래에 read_only_fields 튜플

    class Meta:
        model = Article
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    # 없는 필드(댓글 개수)를 만들어서 JSON을 구성하자. => QuerySet API 코드를 string 으로 넘김
    comment_count = serializers.IntegerField(source='comments.count')
    class Meta:
        model = Article
        fields = ('pk', 'title', 'comment_count')
        read_only_fields = fields
