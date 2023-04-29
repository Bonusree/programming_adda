 # from django.shortcuts import render
# from django.shortcuts import render,HttpResponse,redirect
# from django.contrib.auth.models import User
# from .models import Account
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.decorators import login_required
# from django.utils import timezone
# from django.core.exceptions import ValidationError

# # @login_required
# def register(request):
#     if request.method=="POST":
#         # if registered successfully render to home
#         # else show error message and render to register
#         try:
#             name=request.POST.get("name")
#             email=request.POST.get("email")
#             password=request.POST.get("password")
#             cpassword=request.POST.get("cpassword")
#             if password!=cpassword:
#                 context = {'type':'error','message':'missmatch password!'}
#                 return render(request, 'register.html', context=context)
#             my_user=Account.objects.create_user(name=name, email=email, password=password,role='contestant',joinedDate=timezone.now())
#             my_user.save()
#             context = {'type':'success','message':'You registered successfully. Now login here.'}
#             return render(request, 'login.html', context=context)
#         except ValidationError as e:
#             print('validation error',e.message)
#             context={'type':'error','message':e.message}
#             return render(request, 'register.html',context=context)
#         except ValueError as e:
#             print('value error',e.message)
#             context={'type':'error','message':e.message}
#             return render(request, 'register.html',context=context)
#     else:
#         return render(request, 'register.html')
# from django.shortcuts import render
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render,HttpResponse,redirect
# from account.models import Account
# def login(request):
#     return render(request,'login.html')

# def home(request):
#     if request.method=="POST":
#         email=request.POST.get("email")
#         password=request.POST.get("password")
#         ex=Account.objects.filter(email=email, password=password).exists()
#         print(ex)
#         user=authenticate(request,email=email,password=password)
#         print(user)
#         if user is not None:
#             return render(request, 'home.html')
            
#         else:
#             return HttpResponse("you are not registered")
#     else:
#         return render(request, 'home.html')
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@csrf_protect
def loginPage(request):
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
        
    return render (request,'login.html')

def SignupPage(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('cpassword')
        print(pass1 ,pass2)
        

        my_user=User.objects.create_user(email, email,pass1)
        my_user.save()
        return redirect('login')
    return render (request,'register.html')

def homePage(request):
    context = request.session.get('context', None)
    if context!=None:
        del request.session['context']
    return render (request,'home.html',context=context)

def LogoutPage(request):
    logout(request)
    return redirect('login')



# temporary
def add_editorial(request):
    return render(request, 'add_editorial.html')

def add_blogs(request):
    return render(request, 'add_blogs.html')

def add_problems(request):
    return render(request, 'add_problems.html')