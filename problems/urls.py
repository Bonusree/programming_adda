from django.urls import path
from problems import views 


urlpatterns = [
    path('problems/',views.problems, name='problems'),
]
