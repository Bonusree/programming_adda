from django.urls import path
from editorials import views 


urlpatterns = [
    path('addeditorial/', views.add_editorial, name='add_editorial'),
    path('editorials/',views.editorials, name='editorials'),
    path('search-editorial/', views.search_editorial, name='search_editorial'),
]
