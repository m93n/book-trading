from django.urls import path

from books import views

urlpatterns = {
    path('list/', views.BookList.as_view())
}