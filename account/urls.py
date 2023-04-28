from django.urls import path
from account import views 

from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('register/',views.SignupPage, name='register'),
    path('login/', views.loginPage, name='login'),
    
    path('addblogs/', views.add_blogs, name='addblogs'),
    path('addproblems/', views.add_problems, name='addproblems'),
    
    path('', views.homePage, name="home")
]
