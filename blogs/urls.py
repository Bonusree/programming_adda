from django.urls import path
from blogs import views 


urlpatterns = [
    path('blogs/',views.blogs, name='blogs'),
    path('add-blogs/',views.add_blogs,name='add_blogs')
]
