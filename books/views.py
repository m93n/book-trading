from django.views.generic import ListView, DetailView

from books.models import Book

class BookList(ListView):
    model = Book
    
class BookDetail(DetailView):
    model = Book