from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Books
# Create your views here.
def index(request):
    obj = Books.objects.get(id=1)

    context={
        'title':obj.title,
        'author':obj.author,
        'img':obj.img,
        'variable':"this is sent"
    }
    
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def bestseller(request):
    return render(request,'bestseller.html')

def Feed(request):
     if request.method=="POST":
        title=request.POST.get('title')
        author=request.POST.get('author')
        price=request.POST.get('price')
        desc=request.POST.get('desc')
        rating=request.POST.get('rating')
        review=request.POST.get('review')
        img=request.POST.get('img')
        book_type=request.POST.get('book_type')
        Feed=Books( title=title,author=author,price=price,desc=desc,rating=rating,review=review,img=img,book_type=book_type)
        Feed.save()
     return render(request,'Feed.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact( name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
    return render(request,'contact.html')

def me(request):
    return HttpResponse("i am very good person")