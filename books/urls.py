from django.urls import path

from books import views

urlpatterns = {
    path('list/', views.BookList.as_view()),
    path('detail/<int:pk>', views.BookDetail.as_view()),
}