from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
  path("", views.index,name='home'),  
   
path("about", views.about,name='about'),  
path("bestseller", views.bestseller,name='bestseller'),
path("contacts", views.contacts,name='contacts'),  
path("me", views.me,name='me'), 
    
]
