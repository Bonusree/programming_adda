from django.urls import path
from account import views 

from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('register/',views.SignupPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('', views.homePage, name="home")
]
