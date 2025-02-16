from django.shortcuts import render

# Create your views here.
# suppliers/views.py
from django.views.generic import ListView, DetailView
from .models import Supplier

class SupplierListView(ListView):
    model = Supplier
    template_name = 'suppliers/supplier_list.html'
    context_object_name = 'suppliers'

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'suppliers/supplier_detail.html'
    context_object_name = 'supplier'
