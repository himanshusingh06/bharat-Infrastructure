from django.db import models

# Create your models here.
from django.db import models
from suppliers.models import Supplier

class Material(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity_available = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name