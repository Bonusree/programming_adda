from django.shortcuts import render

# Create your views here.

def others(request):
    return render(request,'others.html')