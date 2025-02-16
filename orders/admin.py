from django.contrib import admin
from .models import Order
# Register your models here.
# Register the Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'material', 'customer_name', 'order_date')  # Customize these fields
    search_fields = ('material', 'customer_name')  # Enable search functionality
    list_filter = ('order_date', 'status')  # Add filters for better navigation
