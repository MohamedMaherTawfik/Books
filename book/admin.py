from django.contrib import admin
from .models import author,book,review
# Register your models here.


class bookadmin(admin.ModelAdmin):
    list_display=['title','publish_date','price']
    search_fields=['title','price']
    list_filter=['publish_date','price']
    
    

admin.site.register(book,bookadmin)
admin.site.register(author)
admin.site.register(review)