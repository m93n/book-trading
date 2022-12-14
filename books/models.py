from django.db import models
from django.conf import settings

User_Model = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Translator(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Language(models.Model):
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.language

class Book(models.Model):
    image = models.ImageField(upload_to="images/", blank=True)
    name = models.CharField(max_length=30)
    introduction = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    translated = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    translators = models.ManyToManyField(Translator, blank=True)
    Release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


#// FUTURE UPDATES

# class UserBook(models.Model):
#     TRADING_TYPE = [
#         ("sell", "sell"),
#         ("lend", "lend"),
#         ("exchange", "exchange"),
#         ("donate", "donate"),
#     ]

#     TAG = [
#         ("I have","I have"),
#         ("I am reading","I am reading"),
#         ("I will read","I will read"),
#         ("I read","I read"),
#     ]
#     user         = models.ForeignKey(User_Model, on_delete=models.CASCADE)
#     book         = models.ForeignKey(Book, on_delete=models.CASCADE)
#     new          = models.BooleanField()
#     trading_type = models.CharField(max_length=10, choices=TRADING_TYPE, null=True, blank=True)
#     tag          = models.CharField (max_length=12, choices=TAG, default='I read')
#     status       = models.ForeignKey('BookStatus', on_delete=models.CASCADE, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     last_updated =  models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.book

# class UserBookImage(models.Model):
#     name = models.CharField(max_length=50)
#     book = models.ForeignKey(UserBook, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to="images/")
#     default = models.BooleanField(default=False)

# class HashTag(models.Model):
#     name = models.CharField(max_length=30)

# class BookStatus(models.Model):
#     STATUS_TYPE = [
#         ("sold","sold"),
#         ("borrowed","borrowed"),
#         ("loaned","loaned"),
#     ]
#     status = models.CharField(max_length=15, choices=STATUS_TYPE)
#     status_date = models.DateField()
