import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from book.models import author,book,review
import random
from faker import Faker


def create_author(n):
    fake=Faker()
    for _ in range(n):
        author.objects.create(
            name=fake.name(),
            biography=fake.text(),
        )
    print(f"{n} Authors was added successufully")
    
  
def create_book(n):
    fake=Faker()
    money=['100','200','150','120','140','170']
    date=['2018','2017','2019','2020','2021','2022','2023']
    for _ in range(n):
        book.objects.create(
            title=fake.name(),
            price=f"{money[random.randint(0,5)]}",
            publish_date= random.randint(date)
        )  
    print(f"{n} Books was added successufully")  
      

def create_review(n):
    fake=Faker()
    rate=['1','2','3','4','5']
    for _ in range(n):
        review.objects.create(
            reviewer_name=fake.name(),
            content=fake.text(),
            rating=f"{rate[random.randint(0,4)]}"
        )        
    print(f"{n} Reviews was added successufully")     


  
        
        
#create_author(25)
create_book(100)
#create_review(30)        