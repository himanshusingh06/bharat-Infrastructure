from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'contractor', 'status', 'start_date', 'end_date')
    search_fields = ('name', 'contractor__name')
    list_filter = ('status', 'start_date', 'end_date')
