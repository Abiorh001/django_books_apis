from django.shortcuts import render
from books.models import Book
from books.serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

# using ApiView to list all books
class BookViews(APIView):

    def get(self, request):
        queryset = Book.objects.all()
        book_serializer = BookSerializer(queryset, many=True)
        return Response(book_serializer.data)
    
# using generic ApiView to list all books
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

