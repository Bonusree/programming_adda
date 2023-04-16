# from django.db import models

# # Create your models here.
# class Account(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.CharField(primary_key=True,max_length=50)
#     password = models.CharField(max_length=50)
#     role = models.CharField(max_length=50)
    
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        if self.filter(email=email).exists():
            raise ValidationError('This email is already in use.')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Account(AbstractBaseUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, primary_key=True)
    password = models.CharField(max_length=150)
    joinedDate = models.DateField(max_length=50)
    role = models.CharField(max_length=50)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.role

