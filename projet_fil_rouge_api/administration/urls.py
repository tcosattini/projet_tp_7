from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    #Onglet "Objets" --- Madani
    re_path(r'^ongletObjets/(?P<idx>[0-9]+)$', views.ongletObjets, name='ongletObjets'),
    re_path(r'^ajoutObjet/(?P<idx>[0-9]+)_(?P<nomValue>[a-zA-Z0-9 ]+)_(?P<poidsValue>[0-9.]+)_(?P<impValue>[0-9]+)_(?P<publicitaireValue>[0-9.]+)_(?P<conditionnementValue>[0-9]+)_(?P<pointsValue>[0-9]+)$', views.ajoutObjet, name='ajoutObjet'),
    re_path(r'^modificationObjet/(?P<idx>[0-9]+)_(?P<idObjetValue>[0-9]+)_(?P<nomValue>[a-zA-Z0-9 ]*)_(?P<poidsValue>[0-9.]*)_(?P<impValue>[0-9]*)_(?P<publicitaireValue>[0-9.]*)_(?P<conditionnementValue>[0-9]*)_(?P<pointsValue>[0-9]*)$', views.modificationObjet, name='modificationObjet'),
    re_path(r'^statusObjet/(?P<idx>[0-9]+)_(?P<idObjetValue>[0-9]+)_(?P<statusValue>[0-1])$', views.statusChangeObjet, name='statusChangeObjet'),

    #Onglet "Emballages" --- Madani
    re_path(r'^ongletEmballages/(?P<idx>[0-9]+)$', views.ongletConditionnement, name='ongletEmballages'),
    re_path(r'^ajoutConditionnement/(?P<idx>[0-9]+)_(?P<nomValue>[a-zA-Z0-9 ]+)_(?P<poidsValue>[0-9]+)_(?P<tarifValue>[0-9.]+)$', views.ajoutConditionnement, name='ajoutConditionnement'),
    re_path(r'^modificationConditionnement/(?P<idx>[0-9]+)_(?P<idConditionnementValue>[0-9]+)_(?P<nomValue>[a-zA-Z0-9 ]*)_(?P<poidsValue>[0-9]*)_(?P<tarifValue>[0-9.]*)$', views.modificationConditionnement, name='modificationConditionnement'),

    #Onglet "Communes" --- Madani
    re_path(r'^ongletCommunes/(?P<idx>[0-9]+)$', views.ongletCommunes, name='ongletCommunes'),
    re_path(r'^ajoutCommune/(?P<idx>[0-9]+)_(?P<communesValue>[a-zA-Z ]+)_(?P<depValue>[0-9]+)_(?P<cpValue>[a-zA-Z0-9 ]+)$', views.ajoutCommune, name='ajoutCommune'),
    re_path(r'^modificationCommune/(?P<idx>[0-9]+)_(?P<idCommuneValue>[0-9]+)_(?P<communesValue>[a-zA-Z ]*)_(?P<depValue>[0-9]*)_(?P<cpValue>[a-zA-Z0-9 ]*)$', views.modificationCommune, name='modificationCommune'),


    #path('', views.index, name='index'),    
    re_path(r'^pagePoids/(?P<idx>[0-9]+)$', views.pagePoids, name='pagePoids'),
    re_path(r'^ajoutPoids/(?P<idx>[0-9]+)_(?P<valmin>[0-9.]+)_(?P<valtimbre>[0-9.]+)', views.ajoutPoids, name='ajoutPoids'),
    re_path(r'^modifierPoids/(?P<idx>[0-9]+)_(?P<id>[0-9.]+)_(?P<valmin>[0-9.]+)_(?P<valtimbre>[0-9.]+)',views.modifierPoids, name='modifierPoids'),
    re_path(r'^pagePoidsVignettes/(?P<idx>[0-9]+)$', views.pagePoidsVignettes, name='pagePoidsVignettes'),
    re_path(r'^ajoutPoidsVignettes/(?P<idx>[0-9]+)_(?P<valmin>[0-9.]+)_(?P<valtimbre>[0-9.]+)', views.ajoutPoidsVignettes, name='ajoutPoidsVignettes'),
    re_path(r'^modifierPoidsVignettes/(?P<idx>[0-9]+)_(?P<id>[0-9.]+)_(?P<valmin>[0-9.]+)_(?P<valtimbre>[0-9.]+)',views.modifierPoidsVignettes, name='modifierPoidsVignettes'),
]
