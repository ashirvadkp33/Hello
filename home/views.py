from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    context={
        'variable':"this is sent"
    }
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def bestseller(request):
    return render(request,'bestseller.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        Email=request.POST.get('Email')
        Phone=request.POST.get('Phone')
        desc=request.POST.get('desc')
        Contact=contact(name=name,Email=Email,Phone=Phone,desc=desc,date=datetime.today())
        Contact.save()
    return render(request,'contact.html')

def me(request):
    return HttpResponse("i am very good person")