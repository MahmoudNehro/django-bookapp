from django.urls import path
from .views import getallbooks,getonebook,add_book,update_book,delete_book

urlpatterns = [
    path('', getallbooks, name="all_books"),
    path('<int:book_id>', getonebook, name="book_page"),
    path('create_book', add_book, name="Add_book"),
    path('update_book/<int:book_id>', update_book, name="update_book"),
    path('delete_book/<int:book_id>', delete_book, name="delete_book"),

]