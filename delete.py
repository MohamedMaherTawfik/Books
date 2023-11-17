import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from book.models import Book

def delete_all_books():
    Book.objects.all().delete()
    