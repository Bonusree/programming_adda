from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from problems.models import Tag, Judge,Problem


class Editorials(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE,null=True)
    editorial_description = models.TextField()
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)