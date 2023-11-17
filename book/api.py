from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from .seralizers import bookserializer,Authorsserializers,Rewviewserializer
from .models import Book,Author,Review
from rest_framework import status
from rest_framework.response import Response


ERORR_404 = {
    "status": '404 not found',
    "message": "something went error, this page not found or the object you want has been deleted"
}



class booklistapi(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=bookserializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['title','publish_date','price']
    search_fields =['title','price','name']
    ordering_fields =['price']
    
class bookdetailapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    lookup_field='pk'
    serializer_class=bookserializer  
    
    def get(self, request, **kwargs):
        try:
            book=Book.objects.get(id=kwargs['pk'])
        except Author.DoesNotExist:
            return Response(ERORR_404,status=status.HTTP_404_NOT_FOUND)
        Book_serializer=bookserializer(book)
        reviews=Review.objects.filter(book=book) 
        reviews_serializer=Rewviewserializer(reviews, many=True)
        return Response({
            'book':Book_serializer.data,
            'reviews':reviews_serializer.data,
        },status=status.HTTP_200_OK)
        

class Authorlistapi(generics.ListAPIView):
    queryset=Author.objects.all()
    serializer_class=Authorsserializers
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['name','birth_date','biography']
    search_fields =['name']

class Authordetailapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    lookup_field = 'pk'
    serializer_class=Authorsserializers  
    
    # def get(self,request, **kwargs):
    #     try:
    #         Author=Author.objects.get(id=kwargs['pk'])
    #     except Author.DoesNotExist:
    #         return Response(ERORR_404,status=status.HTTP_404_NOT_FOUND)
    #     author_serializer=Authorsserializers(Author)
    #     books=Book.objects.filter(Author=Author)
    #     book_serializer=bookserializer(books, many=True)
    #     return Response({
    #         'Author':author_serializer.data,
    #         'books':book_serializer.data,
    #     },status=status.HTTP_200_OK)
    
    
class Reviewlistapi(generics.ListAPIView):
    queryset=Review.objects.all()
    serializer_class=Rewviewserializer   
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter] 
    filterset_fields=['reviewer_name','rating']
    search_fields=['rating']
    
class ReviewDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=Rewviewserializer