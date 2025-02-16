from django.db import models
from projects.models import Project
from orders.models import Order

class Payment(models.Model):
    payment_type = models.CharField(max_length=20, choices=[('project', 'Project'), ('order', 'Order')])
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Payment - {self.payment_type}"