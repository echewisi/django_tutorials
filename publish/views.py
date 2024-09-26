from rest_framework import generics
from .models import Author, Books, Review
from .serializers import AuthorSerializer, BookSerializer, ReviewSerializers
from django.db.models import Count, Avg, Case, When, BooleanField

# List of all authors with their book count
class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.annotate(book_count=Count('book'))
    serializer_class = AuthorSerializer

# List of all books with authors using select_related for optimization
class BookListView(generics.ListAPIView):
    queryset = Books.objects.select_related('author').all()
    serializer_class = BookSerializer

# List of all reviews with books and authors using prefetch_related for optimization
class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.prefetch_related('book__author').all()
    serializer_class = ReviewSerializers

# List of authors who have written more than 1 book
class AuthorsWithMultipleBooksView(generics.ListAPIView):
    queryset = Author.objects.annotate(book_count=Count('book')).filter(book_count__gt=1)
    serializer_class = AuthorSerializer

# List of books with a boolean field 'has_reviews' to indicate if a book has reviews
class BookWithReviewsView(generics.ListAPIView):
    queryset = Books.objects.annotate(
        has_reviews=Case(
            When(review__isnull=False, then=True),
            default=False,
            output_field=BooleanField()
        )
    )
    serializer_class = BookSerializer

# Top 3 authors based on the number of books
class TopAuthorsView(generics.ListAPIView):
    queryset = Author.objects.annotate(book_count=Count('book')).order_by('-book_count')[:3]
    serializer_class = AuthorSerializer
