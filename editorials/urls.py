from django.urls import path
from editorials import views 


urlpatterns = [
    path('editorials/',views.editorials, name='editorials'),
    path('addeditorial/', views.add_editorial, name='addeditorial'),
    path('after_add_editorial/', views.after_add_editorial, name='after_add_editorial'),
    
]
