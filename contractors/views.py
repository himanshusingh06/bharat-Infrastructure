from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Contractor

class ContractorListView(ListView):
    model = Contractor
    template_name = 'contractors/contractor_list.html'
    context_object_name = 'contractors'

class ContractorDetailView(DetailView):
    model = Contractor
    template_name = 'contractors/contractor_detail.html'
    context_object_name = 'contractor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data if needed, e.g., related projects
        context['projects'] = self.object.project_set.all() # Assuming Project has a ForeignKey to Contractor
        return context