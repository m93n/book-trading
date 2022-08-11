from django.db import models
from users.models import UserInfo

class Book(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    description = models.TextField()
    populer_tag = models.BooleanField()

class UserBook(models.Model):
    TRADING_TYPE = [
        ('sell','sell'),
    ]
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    new = models.BooleanField()
    trading_type = models.CharField(max_length=10, choices=TRADING_TYPE)

class UserBookImage(models.Model):
    name = models.CharField(max_length=50)
    book = models.ForeignKey(UserBook, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)
