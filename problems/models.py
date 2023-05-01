from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255)
    valid = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Judge(models.Model):
    name = models.CharField(max_length=255)
    valid = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Problem(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    editorial_link = models.URLField(null=True)
    editorial = models.ForeignKey(Judge, on_delete=models.CASCADE, null=True,related_name="editorials")
    judge = models.ForeignKey(Judge, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
