from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book


class BookTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Django for beginners",
            subtitle="Build websites with Python and Django",
            author="William S. Vincent",
            isbn="938493099501"
        )

    def test_books_views(self):
        url = reverse("books_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{'title': 'Django for beginners', 'subtitle': 'Build websites with Python and Django', 'author': 'William S. Vincent', 'isbn': '938493099501'}])
        self.assertEqual(Book.objects.count(), 1)
