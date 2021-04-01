from .models import Article, Comment
from django import forms

class ArticleForm(forms.ModelForm):
    # Form => HTML만들기, 데어터 검증하기
    # fields에 없는 속성은 html도 안만들고 데이터 검증또한 안합니다.
    # wow라는 이름의 input tag도 만들고 넘어온 데이터 검증도 합니다. 다만 DB에 들어갈 곳이 없음
    wow = forms.CharField(min_length=2, max_length=100)
    
    # content라는 이름의 input type=email, 넘어온 데이터도 email규격에 대해 검증 o, DB에 들어감.
    # 검증해라 => email인지 검증해라
    content = forms.EmailField()
    class Meta:
        model = Article
        fields = ('content', )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', )