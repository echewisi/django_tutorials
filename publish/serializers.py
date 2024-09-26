from rest_framework import serializers
from .models import Author, Books, Review


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields= "__all__"
    
class BookSerializer(serializers.ModelSerializer):
    author= AuthorSerializer()
    class Meta:
        model= Books
        fields= "__all__"

class ReviewSerializers(serializers.ModelSerializer):
    book= BookSerializer()
    
    class Meta:
        model= Review
        fields= "__all__"