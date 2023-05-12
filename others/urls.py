from django.urls import path
from others import views 


urlpatterns = [
    path('others/', views.others, name='others'),
]
