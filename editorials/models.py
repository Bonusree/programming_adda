from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from problems.models import Tag, Judge


class add_editorials(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    judge = models.ForeignKey(Judge, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    tutorial = models.TextField()
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
