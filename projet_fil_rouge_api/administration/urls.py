from django.urls import path, re_path
from . import views

urlpatterns = [
    path('/', views.home, name='home'),

    # Onglet "Objets" --- Madani
    path("/ongletObjets/", views.ongletObjets, name='ongletObjets'),
    re_path(r'^/ajoutObjet/(?P<nomValue>[a-zA-Z0-9 ]+)_(?P<poidsValue>[0-9.]+)_(?P<impValue>[0-9]+)_(?P<publicitaireValue>[0-9.]+)_(?P<conditionnementValue>[0-9]+)_(?P<pointsValue>[0-9]+)$', views.ajoutObjet, name='ajoutObjet'),
    re_path(r'^/modificationObjet/(?P<idObjetValue>[0-9]+)_(?P<nomValue>[a-zA-Z0-9 ]*)_(?P<poidsValue>[0-9.]*)_(?P<impValue>[0-9]*)_(?P<publicitaireValue>[0-9.]*)_(?P<conditionnementValue>[0-9]*)_(?P<pointsValue>[0-9]*)$',
            views.modificationObjet, name='modificationObjet'),
    re_path(r'^/statusObjet/(?P<idObjetValue>[0-9]+)_(?P<statusValue>[0-1])$',
            views.statusChangeObjet, name='statusChangeObjet'),

    # Onglet "Emballages" --- Madani
    path("/ongletEmballages/", views.ongletEmballages, name='ongletEmballages'),
    re_path(r'^/ajoutConditionnement/(?P<nomValue>[a-zA-Z0-9 ]+)_(?P<poidsValue>[0-9]+)_(?P<tarifValue>[0-9.]+)$',
            views.ajoutConditionnement, name='ajoutConditionnement'),
    re_path(r'^/modificationConditionnement/(?P<idConditionnementValue>[0-9]+)_(?P<nomValue>[a-zA-Z0-9 ]*)_(?P<poidsValue>[0-9]*)_(?P<tarifValue>[0-9.]*)$',
            views.modificationConditionnement, name='modificationConditionnement'),

    # Onglet "Communes" --- Madani
    path("/ongletCommunes/", views.ongletCommunes, name='ongletCommunes'),
    re_path(r'^/ajoutCommune/(?P<communesValue>[a-zA-Z ]+)_(?P<depValue>[0-9]+)_(?P<cpValue>[a-zA-Z0-9 ]+)$',
            views.ajoutCommune, name='ajoutCommune'),
    re_path(r'^/modificationCommune/(?P<idCommuneValue>[0-9]+)_(?P<communesValue>[a-zA-Z ]*)_(?P<depValue>[0-9]*)_(?P<cpValue>[a-zA-Z0-9 ]*)$',
            views.modificationCommune, name='modificationCommune'),

]
