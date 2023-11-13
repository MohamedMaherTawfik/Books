from django.urls import path
from .api import booklistapi,bookdetailapi


urlpatterns = [
    path('api/list',booklistapi.as_view()),
    path('api/detail',bookdetailapi.as_view()),
]