from django.db import models
from django.conf import settings

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=150)
    email =models.CharField(max_length=150)
    phone =models.CharField(max_length=150)
    desc =models.TextField()
    date = models.DateField()

book_choice=[('fiction','fiction'),('drama','drama'),('history','history'),('lifestyle','lifestyle'),
('children','children'),('college','college'),('biography','biography')]

class Books(models.Model):
    author=models.CharField( null=True, max_length=200)
    title=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    desc=models.CharField(max_length=500)
    img=models.ImageField(null=True,blank=True,upload_to="static/img")
    rating=models.CharField(max_length=10)
    review=models.CharField(max_length=200)
    book_type=models.CharField(choices=book_choice,max_length=20)
    stock=models.IntegerField(default=0)