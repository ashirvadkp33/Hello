from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
  path("", views.index,name='home'),  
   
path("about", views.about,name='about'),  
path("bestseller", views.bestseller,name='bestseller'),
path("Contact", views.Contact,name='Contact'),  
path("me", views.me,name='me'), 
    
]
