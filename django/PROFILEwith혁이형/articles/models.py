from django.db import models
from django.conf import settings
#  models.py 에서는 settings 자체를 import 해와서 user를 불러야 한다.
# 1 : N 그리고 M : N 관계가 5개가 있다!

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles' )
    # like_users 를 related name 안해주면 매니저가 겹치는 현상 발생.
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content


# Class 3번쨰 컬럼(models.Modle):
    # pass