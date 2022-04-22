from django.shortcuts import render

from books.models import Book
from .models import Author


# Create your views here.
def getoneauthor(request,author_id):
    author = Author.objects.get(id=author_id)
    book_author = Book.objects.filter(author_id=author_id)


    context={
        "Author": author,
        "Book_author":book_author,
    }
    return render (request,'author/authordetails.html',context=context)

