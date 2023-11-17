from rest_framework import serializers
from .models import Book,Author,Review


class bookserializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields = '__all__' 



class Authorsserializers(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields= '__all__'
        
        
class Rewviewserializer(serializers.ModelSerializer):
    class Meta:
        model=Review 
        fields= '__all__' 