from django.db import models
from contractors.models import Contractor

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('ongoing', 'Ongoing'), ('completed', 'Completed')])
    contractor = models.ForeignKey(Contractor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
