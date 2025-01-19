from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    firs_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
