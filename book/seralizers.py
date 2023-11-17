from rest_framework import serializers
from .models import book,author,review


class bookserializer(serializers.ModelSerializer):
    class Meta:
        model= book
        fields = '__all__' 



class Authorsserializers(serializers.ModelSerializer):
    class Meta:
        model=author
        fields= '__all__'
        
        
class Rewviewserializer(serializers.ModelSerializer):
    class Meta:
        model=review 
        fields= '__all__' 