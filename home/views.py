from django.shortcuts import render,HttpResponse

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

def contacts(request):
    return render(request,'contact.html')

def me(request):
    return HttpResponse("i am very good person")