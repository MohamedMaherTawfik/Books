from rest_framework import serializers
from .models import Book,Author,Review


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields = '__all__' 



class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields= '__all__'
        
        
class RewviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review 
        fields= '__all__' 