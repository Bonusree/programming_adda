from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def problems(request):
    if request.method=="POST":
        pass
    else:
        return render(request, 'problems.html')
    
# @login_required
def addproblem(request):
    return render(request,'addproblem.html')