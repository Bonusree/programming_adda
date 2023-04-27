from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Problem(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    judge = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
