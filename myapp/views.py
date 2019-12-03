from rest_framework import viewsets, status
from rest_framework.response import Response

from myapp import serializers
from . import models
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    def create(self, request, format=None):
        book_create = models.Book.objects.all()
        serializer = serializers.BookSerializer(book_create, many=True)
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

    def retrieve(self, reqeust, pk=None, format=None):
        pass

    def update(self, reqeust, pk=None, format=None):
        book_update = models.objects.get(id=pk)
        book_update.save()
        return Response(status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk=None):
        book_delete = models.objects.get(id=pk)
        book_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
