from django.urls import path
from contestants import views 


urlpatterns = [
    path('contestants/',views.contestants, name='contestants'),
    path('profile/',views.profile, name='profile'),
]
