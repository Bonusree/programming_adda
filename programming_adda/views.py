from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect
def login(request):
    return render(request,'login.html')

def home(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(request,emailaddress=email,password=password)
        print(user)
        if user is not None:
            return render(request, 'home.html')
            
        else:
            return HttpResponse("you are not registered")
    else:
        return render(request, 'home.html')

def register(request):
    return render(request,'register.html')

def addproblem(request):
    return render(request,'addproblem.html')

def problems(request):
    return render(request,'problems.html')
