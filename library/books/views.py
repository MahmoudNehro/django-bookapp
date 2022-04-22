from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
# Create your views here.


def getallbooks(request):
    context={
        "Books":Book.objects.all()
    }
    return render (request,'books/books.html',context=context)
def getonebook(request,book_id):
    book=Book.objects.get(id=book_id)
    print(type(book))
    print(book)
    context={
        "Book":book,
    }
    return render (request,'books/bookdetails.html',context=context)



def add_book(request):
    form = BookForm()
    if request.method == "POST":
            form = BookForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("all_books")

    context = {
        'form': form
    }
    return render(request, 'books/book-form.html', context=context)



def update_book(request,book_id):
    book = Book.objects.get(id=book_id)
    form = BookForm(instance=book)
    if request.method == "POST":
            form = BookForm(request.POST, request.FILES, instance = book)
            if form.is_valid():
                form.save()
                return redirect("all_books")
    context = {
        'form': form
    }
    return render(request, 'books/book-form.html', context=context)



def delete_book(request,book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('all_books')
    return render(request, "books/delete_book.html", {'object':book})

