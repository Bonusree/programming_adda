from django.urls import path
from editorials import views 


urlpatterns = [
    path('editorials/',views.editorials, name='editorials'),
]
