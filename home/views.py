from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages 


#password for user is admin admin
#ashish ashish
#silver ssiillvv
#priyanshu priyanshu


# Create your views here.
#added manually
def index(request):
    context={
        'variable1': "This is sent",
        'variable2': "Developer name is AyushG"
    }
    return render(request,'index.html',context)

def login(request): 
    render(request,'login.html')

def logout(request):
    render(request,'index.html')

def about(request):
    return render(request,'about.html')
    
def services(request):
    return render(request,'services.html')
    

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your contact Form has been submitted!')
    return render(request,'contact.html')
    #return HttpResponse("This is contact page.")
