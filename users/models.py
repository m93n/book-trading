from django.db import models
from django.conf import settings

from books.models import Book, HashTag

User_Model = settings.AUTH_USER_MODEL

class UserInfo(models.Model):
    user = models.OneToOneField(User_Model, on_delete=models.CASCADE)
    about_me = models.TextField()
    image = models.ImageField()
    followers = models.ManyToManyField(User_Model, related_name='userinfo_followers')
    following = models.ManyToManyField(User_Model, related_name='userinfo_following')

class Post(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    source = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    src = models.ImageField()
    hashtag = models.ManyToManyField(HashTag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated =  models.DateTimeField(auto_now=True)
    
