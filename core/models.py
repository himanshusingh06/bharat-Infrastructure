from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('contractor', 'Contractor'),
        ('employee', 'Employee'),
        ('vendor', 'Vendor'),
        ('supplier', 'Supplier'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
