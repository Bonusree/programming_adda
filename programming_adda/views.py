from django.shortcuts import render

def login(request):
    return render(request,'login.html')

def home_view(request):
    print('hello my view')
    return render(request,'home.html')


def register(request):
    return render(request,'register.html')

def addproblem(request):
    return render(request,'addproblem.html')
