from django.urls import path
from .api import booklistapi,bookdetailapi
from .api import Authorlistapi,Authordetailapi
from .api import Reviewlistapi,ReviewDetailApi
from .views import book

urlpatterns = [
    path('api/listbook',booklistapi.as_view()),
    path('api/listbook/<int:pk>',bookdetailapi.as_view()),
    
    path('api/listauthor',Authorlistapi.as_view()),
    path('api/listauthor/<int:pk>',Authordetailapi.as_view()),
    
    path('api/listreview',Reviewlistapi.as_view()),
    path('api/listreview/<int:pk>',ReviewDetailApi.as_view()),
    
]