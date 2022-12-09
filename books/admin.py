from django.contrib import admin

from books import models

admin.site.register(models.Book)
admin.site.register(models.Category)
admin.site.register(models.Author)
admin.site.register(models.Translator)
admin.site.register(models.Language)
