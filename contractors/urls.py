# contractors/urls.py
from django.urls import path
from .views import ContractorListView, ContractorDetailView

urlpatterns = [
    path('', ContractorListView.as_view(), name='contractor-list'),
    path('<int:pk>/', ContractorDetailView.as_view(), name='contractor-detail'),
]
