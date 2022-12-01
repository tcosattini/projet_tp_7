from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    data_communes = TCommunes.objects.all()
    context = {
        "Communes" : data_communes,
    }
    return render(request, 'page.html', context)

def ajoutCommune(request, communesValue, depValue, cpValue):
    ajoutCommune = TCommunes(dep = depValue, cp = cpValue, communes = communesValue)
    ajoutCommune.save()
    return render(request, 'retour.html', )

def modificationCommune(request, idCommuneValue, communesValue, depValue, cpValue):
    TCommunes.objects.filter(id_commune = idCommuneValue).delete()
    ajoutCommune = TCommunes(id_commune = idCommuneValue, dep = depValue, cp = cpValue, communes = communesValue)
    ajoutCommune.save()
    return render(request, 'retour.html', )

def index2(request):
    data_conditionnements = TConditionnement.objects.all()
    context = {
        "Conditionnements" : data_conditionnements,
    }
    return render(request, 'page2.html', context)

def ajoutConditionnement(request, nomValue, poidsValue, tarifValue):
    ajoutConditionnement = TConditionnement(libcondit = nomValue, poidscondit = poidsValue, prixcond = tarifValue)
    ajoutConditionnement.save()
    return render(request, 'retour2.html', )

def modificationConditionnement(request, idConditionnementValue, nomValue, poidsValue, tarifValue):
    TConditionnement.objects.filter(idcondit = idConditionnementValue).delete()
    ajoutConditionnement = TConditionnement(idcondit = idConditionnementValue, libcondit = nomValue, poidscondit = poidsValue, prixcond = tarifValue)
    ajoutConditionnement.save()
    return render(request, 'retour2.html', )