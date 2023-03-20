from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required(login_url='home')
def register(request):
    return render(request, 'register.html')

def login(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        c_password=request.POST.get("c_password")
        if password!=c_password:
            msg="password doesn't matched"
            return render(request, 'register.html', {'msg':msg})
        my_user=User.objects.create_user(name, email, password)
        my_user.save()
        return render(request, 'login.html')
    else:
        return render(request, 'register.html')

def home(request):
    if request.method=="POST":
        name=request.POST.get("name")
        password=request.POST.get("password")
        user=authenticate(request,username=name,password=password)
        if user is not None:
            return HttpResponse("you are not registered")
        else:
            return HttpResponse("welcome")
    else:
        return render(request, 'login.html')
        