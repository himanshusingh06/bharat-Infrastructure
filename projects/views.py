from django.shortcuts import render

# Create your views here.
# projects/views.py
from django.views.generic import ListView, DetailView
from .models import Project

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data if needed, e.g., related orders, payments
        # Example:
        # context['orders'] = self.object.order_set.all()  # If Project has a relationship to Order
        return context
