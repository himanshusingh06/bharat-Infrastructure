from django.db import models
class Supplier(models.Model):
    business_name = models.CharField(max_length=100,default="", blank=True)
    contact_person = models.CharField(max_length=100,default="Unknown", blank=True)
    phone = models.CharField(max_length=15,default=123, blank=True)
    email = models.EmailField(unique=True,default="", blank=True)
    address = models.TextField(default="", blank=True)

    def __str__(self):
        return self.business_name

