from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
import json
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


@permission_classes([IsAuthenticated])  # Only logged-in users can modify books
@csrf_exempt  # Disable CSRF for this API
@api_view(['GET', 'POST'])
def get_books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = json.loads(request.body)  # Convert JSON to Python dictionary
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])  # Only logged-in users can access this
@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)  # Get book or return 404

    if request.method == 'GET':  # Retrieve a single book
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':  # Update book
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':  # Delete book
        book.delete()
        return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
