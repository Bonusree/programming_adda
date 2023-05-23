from django.urls import path
from graphics import views 

from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('graphics/', views.graphics, name='graphics'),
    path('graphics-circle/', views.graphics_circle, name='graphics_circle'),
]
