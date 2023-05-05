from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from problems.models import Problem


class Blogs(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField()
    related_problem = models.ManyToManyField(Problem,blank=True)
    additional_comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
