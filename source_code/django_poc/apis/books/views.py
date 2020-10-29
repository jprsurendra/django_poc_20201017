from rest_framework import viewsets, generics

from apis.books.models import Books
from apis.books.serializers import BookSerializer

class BooksModelViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer