from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

# password for user is admin admin
# silver ssiillvv
# priyanshu priya123


# Create your views here.
#added manually
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')


def loginUser(request): 
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            # A backend authenticated the credentials
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'about.html')
    
def services(request):
    if request.user.is_anonymous:
        return redirect("/login")
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

def pcb(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'pcb.html')