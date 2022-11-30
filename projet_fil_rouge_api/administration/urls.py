from django.contrib import admin
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', views.index, name='index'),
    path('page2.html', views.index2, name='index2'),
    re_path(r'^ajoutCommune/(?P<communesValue>[a-zA-Z ]+)_(?P<depValue>[0-9]+)_(?P<cpValue>[a-zA-Z0-9 ]+)$', views.ajoutCommune, name='ajoutCommune'),
    re_path(r'^modificationCommune/(?P<idCommuneValue>[0-9]+)_(?P<communesValue>[a-zA-Z ]+)_(?P<depValue>[0-9]+)_(?P<cpValue>[a-zA-Z0-9 ]+)$', views.modificationCommune, name='modificationCommune'),
]