from django.contrib import admin
from .models import Material
# Register your models here.
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Customize these fields
    search_fields = ('name',)  # Enable search functionality
    list_filter = ('name',)  # Add filters for better navigation