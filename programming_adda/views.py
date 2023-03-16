from django.shortcuts import render

def home_view(request):
    print('hello my view')
    return render(request,'home.html')
