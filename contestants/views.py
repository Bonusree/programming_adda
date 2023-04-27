from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# @login_required
def contestants(request):
    if request.method=="POST":
        pass
    else:
        return render(request, 'contestants.html')

def profile(request):
   
    return render(request, 'profile.html')