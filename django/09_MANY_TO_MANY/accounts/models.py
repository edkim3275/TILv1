from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    fans = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='stars')
    
    # profile_pic = models.ImageField()
    # freinds = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return f'{self.pk}: {self.username}'

