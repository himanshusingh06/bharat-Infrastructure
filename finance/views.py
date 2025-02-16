from django.shortcuts import render

# Create your views here.
# finance/views.py
from django.views.generic import ListView, DetailView
from .models import Payment

class PaymentListView(ListView):
    model = Payment
    template_name = 'finance/payment_list.html'
    context_object_name = 'payments'

class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'finance/payment_detail.html'
    context_object_name = 'payment'
