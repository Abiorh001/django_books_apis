from django.urls import path
from books.views import BookViews, BookList

urlpatterns = [
    path('all_books', BookViews.as_view(), name="books_list"),
    path('', BookList.as_view(), name="books_list"),
    
]