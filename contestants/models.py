from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_sites(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=150)
    

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(null=True,max_length=50)
    bio = models.TextField(null=True,max_length=400)
    url = models.ManyToManyField(User_sites,blank=True)
