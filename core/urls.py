from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # The home view mapped to the root URL
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
