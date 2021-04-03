from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    stars = models.ManyToManyField('self', symmetrical=False, related_name='fans')

    # __str__ 이 할아버지 클래스에 있어서 굳이 여긴 해줄 필요가 없다.
    # 그래서 DTL에서 request.user 까지만 쳐도 request.user.username 을 봤던 것이다!