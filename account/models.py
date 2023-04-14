from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(primary_key=True,max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)