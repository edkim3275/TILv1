from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now_add : 생성 되었을 때만
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now : 계속해서 바뀌는 값
    updated_at = models.DateTimeField(auto_now=True)
