from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books.api.views import (
        BookViewSet
    )

router = DefaultRouter()
router.register(r'titlebooks', BookViewSet, basename='title_of_books')
urlpatterns = [
    path('', include(router.urls))
]