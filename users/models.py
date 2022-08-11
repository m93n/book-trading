from django.db import models
from django.contrib.auth.models import User
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    aboutme = models.TextField()
    image = models.ImageField()
    followers = models.ManyToManyField(User, related_name='userinfo_followers')
    following = models.ManyToManyField(User, related_name='userinfo_following')

class Post(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
