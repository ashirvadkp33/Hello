from django.db import models
from django.conf import settings

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=150)
    Email =models.CharField(max_length=150)
    Phone =models.CharField(max_length=150)
    desc =models.TextField()
    date = models.DateField()
