from django.shortcuts import render
from .models import Book 
# Create your views here.


def book(request):
    all_books=Book.objects.all()
    return render(request,'book.html',{'books':all_books})
