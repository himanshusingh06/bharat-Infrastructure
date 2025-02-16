from django.db import models

# Create your models here.
from django.db import models
from core.models import UserProfile



class Contractor(models.Model):
    name = models.CharField(max_length=100, default="Unknown",blank=True)
    phone = models.CharField(max_length=15, default=12345,blank=True)
    email = models.EmailField(default="example@gmail.com")
    address = models.TextField(default="NA",blank=True)

    def __str__(self):
        return self.name

