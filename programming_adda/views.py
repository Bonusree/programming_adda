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
#         user=authenticate(request,emailaddress=email,password=password)
#         print(user)
#         if user is not None:
#             return render(request, 'home.html')
            
#         else:
#             return HttpResponse("you are not registered")
#     else:
#         return render(request, 'home.html')

# def register(request):
#     return render(request,'register.html')

