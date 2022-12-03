from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# @login_required


def home(request):
    return render(request, template_name='home.html')


# Onglet "Objets" --- Madani ---

def ongletObjets(request):
    data_objet = TObjet.objects.all()
    context = {
        "Objets": data_objet,
    }
    return render(request, 'onglet_objets.html', context)


def ajoutObjet(request, nomValue, poidsValue, impValue, publicitaireValue, conditionnementValue, pointsValue):
    ajoutObjet = TObjet(libobj=nomValue, poidsobj=poidsValue, o_imp=impValue,
                        puobj=publicitaireValue, idcondit=conditionnementValue, points=pointsValue, is_active=1)
    ajoutObjet.save()
    return render(request, 'retour_objets.html', )


def modificationObjet(request, idObjetValue, nomValue, poidsValue, impValue, publicitaireValue, conditionnementValue, pointsValue):
    if (nomValue != ""):
        TObjet.objects.filter(codobj=idObjetValue).update(libobj=nomValue)
    if (poidsValue != ""):
        TObjet.objects.filter(codobj=idObjetValue).update(poidsobj=poidsValue)
    if (impValue != ""):
        TObjet.objects.filter(codobj=idObjetValue).update(o_imp=impValue)
    if (publicitaireValue != ""):
        TObjet.objects.filter(codobj=idObjetValue).update(
            puobj=publicitaireValue)
    if (conditionnementValue != ""):
        TObjet.objects.filter(codobj=idObjetValue).update(
            idcondit=conditionnementValue)
    if (pointsValue != ""):
        TObjet.objects.filter(codobj=idObjetValue).update(points=pointsValue)
    return render(request, 'retour_objets.html', )


def statusChangeObjet(request, idObjetValue, statusValue):
    TObjet.objects.filter(codobj=idObjetValue).update(is_active=statusValue)
    return render(request, 'retour_objets.html', )


# Onglet "Emballages" --- Madani ---

def ongletEmballages(request):
    data_conditionnements = TConditionnement.objects.all()
    context = {
        "Conditionnements": data_conditionnements,
    }
    return render(request, 'onglet_emballages.html', context)


def ajoutConditionnement(request, nomValue, poidsValue, tarifValue):
    ajoutConditionnement = TConditionnement(
        libcondit=nomValue, poidscondit=poidsValue, prixcond=tarifValue)
    ajoutConditionnement.save()
    return render(request, 'retour_emballages.html', )


def modificationConditionnement(request, idConditionnementValue, nomValue, poidsValue, tarifValue):
    if (nomValue != ""):
        TConditionnement.objects.filter(
            idcondit=idConditionnementValue).update(libcondit=nomValue)
    if (poidsValue != ""):
        TConditionnement.objects.filter(
            idcondit=idConditionnementValue).update(poidscondit=poidsValue)
    if (tarifValue != ""):
        TConditionnement.objects.filter(
            idcondit=idConditionnementValue).update(prixcond=tarifValue)
    return render(request, 'retour_emballages.html', )


# Onglet "Emballages" --- Madani ---

def ongletCommunes(request):
    data_communes = TCommunes.objects.all()
    context = {
        "Communes": data_communes,
    }
    return render(request, 'onglet_communes.html', context)


def ajoutCommune(request, communesValue, depValue, cpValue):
    ajoutCommune = TCommunes(dep=depValue, cp=cpValue, communes=communesValue)
    ajoutCommune.save()
    return render(request, 'retour_communes.html', )


def modificationCommune(request, idCommuneValue, communesValue, depValue, cpValue):
    if (communesValue != ""):
        TCommunes.objects.filter(id_commune=idCommuneValue).update(
            communes=communesValue)
    if (depValue != ""):
        TCommunes.objects.filter(
            id_commune=idCommuneValue).update(dep=depValue)
    if (cpValue != ""):
        TCommunes.objects.filter(id_commune=idCommuneValue).update(cp=cpValue)
    return render(request, 'retour_communes.html', )
