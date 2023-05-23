from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.db.utils import DatabaseError

from django.utils.safestring import mark_safe

from problems.models import Problem
from blogs.models import Blogs
from contestants.models import Profile
# Create your views here.

def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

@csrf_protect
def loginPage(request):
    
    # check session context 
    context = request.session.get('context', None)
    if context!=None:
        del request.session['context']
        
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        print(user)
        if user is not None:
            login(request,user)
            context = {'type':'success','message':'Successfully you are logged in.'}
            request.session['context'] = context
            return redirect('home')
        else:
            context = {'type':'error','message':'Username or Password is incorrect!'}
            return render (request,'login.html', context=context)
        
    return render (request,'login.html',context=context)

def SignupPage(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('cpassword')
        context={'type':'error','message':''}
        
        # check password and confirm password
        if pass1!=pass2:
            context['message']='Password does not match'
            return render(request,'register.html',context=context)
        
        # check duplicate username
        if User.objects.filter(username=name).exists():
            context['message']='Duplicate username'
            return render(request,'register.html',context=context)
        
        # check duplicate email address 
        if User.objects.filter(email=email).exists():
            context['message']='Duplicate email address'
            return render(request,'register.html',context=context)

        try:
            my_user=User.objects.create_user(username=name, email=email,password=pass1)
            my_user.save()
        except DatabaseError as e:
            context['message']=f'Sorry something error with database. Error: {e}'
            return render(request,'register.html',context=context)
        except Exception as e:
            context['message']=f'Sorry something error. Error: {e}'
            return render(request,'register.html',context=context)
        
        context['type']='success'
        context['message']='Your registration successfully completed.'
        request.session['context']=context
        return redirect('login')
    return render (request,'register.html')

def homePage(request):
    context = request.session.get('context', None)
    if context!=None:
        del request.session['context']
    else:
        context = {}
    context['problems']=Problem.objects.count()
    context['blogs']=Blogs.objects.count()
    context['contributors']=Profile.objects.count()
    context['editorials']=0
    return render (request,'home.html',context=context)

def LogoutPage(request):
    logout(request)
    context = {'type':'success','message':'You are logout'}
    return redirect('login')


