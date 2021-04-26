# serializers.py
from django import forms

class ArticleForm(forms.ModelForm):
    title = forms.CharField(min_length=2, max_length=50)
    class Meta:
        model = Article
        fields = '__all__'

# 1. 데이터 검증
# 2. HTML(<form></form>) 생성