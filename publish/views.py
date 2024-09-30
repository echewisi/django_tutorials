from rest_framework import generics
from .models import Author, Books, Review
from .serializers import AuthorSerializer, BookSerializer, ReviewSerializers
from django.db.models import Count, Avg, Case, When, BooleanField, Sum
from django.db.models import Q, F

# List of all authors with their book count
class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.annotate(book_count=Count('books'))
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
    queryset = Author.objects.annotate(book_count=Count('books')).filter(book_count__gt=1)
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
    queryset = Author.objects.annotate(book_count=Count('books')).order_by('-book_count')[:3]
    serializer_class = AuthorSerializer


class AuthorCreateView(generics.CreateAPIView):
    queryset= Author.objects.all()
    serializer_class= AuthorSerializer

class BookCreateView(generics.CreateAPIView):
    queryset= Books.objects.all()
    serializer_class= BookSerializer
    
class ReviewCreateView(generics.CreateAPIView):
    queryset= Review.objects.all()
    serializer_class= ReviewSerializers




#Advanced filtering:
#books where the title starts with 'A' or 'B' and published after 2000
book= Books.objects.filter(
    Q(title__startswith= 'A') | Q(title__startswith= 'B'),
    published_date__year__gt=2000
    
)

#Books where the number of pages is greater than the number of reviews
books= Books.objects.annotate(review_count= Count('review')).filter(pages__gt= F('review_count'))

#this would return books greater than 2010
books_greater_than_2010= Books.objects.filter(published_date__year__gt= 2010)

books= Books.objects.filter(title__icontains= 'Django')