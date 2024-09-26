from django.urls import path
from .views import (
    AuthorListView,
    BookListView,
    ReviewListView,
    AuthorsWithMultipleBooksView,
    BookWithReviewsView,
    TopAuthorsView
)

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('authors/multiple-books/', AuthorsWithMultipleBooksView.as_view(), name='authors-multiple-books'),
    path('books/with-reviews/', BookWithReviewsView.as_view(), name='books-with-reviews'),
    path('authors/top/', TopAuthorsView.as_view(), name='top-authors'),
]
