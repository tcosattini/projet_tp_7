from . import views
from django.urls import path
from django.shortcuts import redirect

urlpatterns = [
    path('', views.home, name='utilisateur.home'),  # must ALWAYS be first
    path('add/', views.add, name='utilisateur.add'),
    path('list/', views.list, name='utilisateur.list'),
    path("toggle/<int:id>", views.toggle_active, name='utilisateur.toggle'),
    path('change/<int:id>', views.change, name='utilisateur.change'),
]
