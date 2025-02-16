from django.contrib import admin
from .models import Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('contact_person', 'business_name', 'phone')
    search_fields = ('business_name', 'phone')


    
