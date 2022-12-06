from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    re_path(r'^pagePoids/(?P<idx>[0-9]+)$', views.pagePoids, name='pagePoids'),
    re_path(r'^ajoutPoids/(?P<idx>[0-9]+)_(?P<valmin>[0-9.]+)_(?P<valtimbre>[0-9.]+)', views.ajoutPoids, name='ajoutPoids'),
    re_path(r'^modifierPoids/(?P<idx>[0-9]+)_(?P<id>[0-9.]+)_(?P<valmin>[0-9.]+)_(?P<valtimbre>[0-9.]+)',views.modifierPoids, name='modifierPoids'),
    re_path(r'^pagePoidsVignettes/(?P<idx>[0-9]+)$', views.pagePoidsVignettes, name='pagePoidsVignettes'),
    re_path(r'^ajoutPoidsVignettes/(?P<idx>[0-9]+)_(?P<valmin>[0-9.]+)_(?P<valtimbre>[0-9.]+)', views.ajoutPoidsVignettes, name='ajoutPoidsVignettes'),
    re_path(r'^modifierPoidsVignettes/(?P<idx>[0-9]+)_(?P<id>[0-9.]+)_(?P<valmin>[0-9.]+)_(?P<valtimbre>[0-9.]+)',views.modifierPoidsVignettes, name='modifierPoidsVignettes'),
]
