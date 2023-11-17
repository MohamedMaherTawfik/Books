from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from .seralizers import bookserializer,Authorsserializers,Rewviewserializer
from .models import book,author,review




class booklistapi(generics.ListAPIView):
    queryset=book.objects.all()
    serializer_class=bookserializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['title','publish_date','price']
    search_fields =['title','price','name']
    ordering_fields =['price']
    
class bookdetailapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=book.objects.all()
    serializer_class=bookserializer  
    
    
    
    
class Authorlistapi(generics.ListAPIView):
    queryset=author.objects.all()
    serializer_class=Authorsserializers
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['name','birth_date','biography']
    search_fields =['name']

class Authordetailapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=author.objects.all()
    serializer_class=Authorsserializers  
    
    
    
    
    
class Reviewlistapi(generics.ListAPIView):
    queryset=review.objects.all()
    serializer_class=Rewviewserializer   
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter] 
    filterset_fields=['reviewer_name','rating']
    search_fields=['rating']
    
class ReviewDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=review.objects.all()
    serializer_class=Rewviewserializer