from django.urls import path
from account import views 


urlpatterns = [
    path('',views.register),
    path('login', views.login, name='login'),
    path('home', views.home, name="home")
]
