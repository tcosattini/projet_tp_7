from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import *
from .forms import *
import math
# @login_required


def home(request):
    return render(request, template_name='home.html')


# Onglet "Objets" --- Madani ---

def ongletObjets(request, idx):
    idx = int(idx)
    t_min = (idx-1)*10
    t_max = (idx)*10
    taille = len(TObjet.objects.all())
    idx_max = math.ceil(taille/10)
    data_objet = TObjet.objects.all()[t_min:t_max]
    context = {
        "Objets": data_objet,
        "Index": idx,
        "Index_max": idx_max,
    }
    return render(request, 'onglet_objets.html', context)


def ajoutObjet(request, idx, nomValue, poidsValue, impValue, publicitaireValue, conditionnementValue, pointsValue):
    ajoutObjet = TObjet(libobj=nomValue, poidsobj=poidsValue, o_imp=impValue,
                        puobj=publicitaireValue, idcondit=conditionnementValue, points=pointsValue, is_active=1)
    ajoutObjet.save()
    return HttpResponseRedirect("/home/ongletObjets/"+idx)


def modificationObjet(request, idx, idObjetValue, nomValue, poidsValue, impValue, publicitaireValue, conditionnementValue, pointsValue):
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
    return HttpResponseRedirect("/home/ongletObjets/"+idx)


def statusChangeObjet(request, idx, idObjetValue, statusValue):
    TObjet.objects.filter(codobj=idObjetValue).update(is_active=statusValue)
    return HttpResponseRedirect("/home/ongletObjets/"+idx)


# Onglet "Emballages" --- Madani ---

def ongletConditionnement(request, idx):
    idx = int(idx)
    t_min = (idx-1)*10
    t_max = (idx)*10
    taille = len(TConditionnement.objects.all())
    idx_max = math.ceil(taille/10)
    data_conditionnements = TConditionnement.objects.all()[t_min:t_max]
    context = {
        "Conditionnements": data_conditionnements,
        "Index": idx,
        "Index_max": idx_max,
    }
    return render(request, 'onglet_emballages.html', context)


def ajoutConditionnement(request, idx, nomValue, poidsValue, tarifValue):
    ajoutConditionnement = TConditionnement(
        libcondit=nomValue, poidscondit=poidsValue, prixcond=tarifValue)
    ajoutConditionnement.save()
    return HttpResponseRedirect("/home/ongletEmballages/"+idx)


def modificationConditionnement(request, idx, idConditionnementValue, nomValue, poidsValue, tarifValue):
    if (nomValue != ""):
        TConditionnement.objects.filter(
            idcondit=idConditionnementValue).update(libcondit=nomValue)
    if (poidsValue != ""):
        TConditionnement.objects.filter(
            idcondit=idConditionnementValue).update(poidscondit=poidsValue)
    if (tarifValue != ""):
        TConditionnement.objects.filter(
            idcondit=idConditionnementValue).update(prixcond=tarifValue)
    return HttpResponseRedirect("/home/ongletEmballages/"+idx)


# Onglet "Emballages" --- Madani ---

def ongletCommunes(request, idx):
    idx = int(idx)
    t_min = (idx-1)*10
    t_max = (idx)*10
    taille = len(TCommunes.objects.all())
    idx_max = math.ceil(taille/10)
    data_communes = TCommunes.objects.all()[t_min:t_max]
    context = {
        "Communes": data_communes,
        "Index": idx,
        "Index_max": idx_max,
    }
    return render(request, 'onglet_communes.html', context)


def ajoutCommune(request, idx, communesValue, depValue, cpValue):
    ajoutCommune = TCommunes(dep=depValue, cp=cpValue, communes=communesValue)
    ajoutCommune.save()
    return HttpResponseRedirect("/home/ongletCommunes/"+idx)


def modificationCommune(request, idx, idCommuneValue, communesValue, depValue, cpValue):
    if (communesValue != ""):
        TCommunes.objects.filter(id_commune=idCommuneValue).update(
            communes=communesValue)
    if (depValue != ""):
        TCommunes.objects.filter(
            id_commune=idCommuneValue).update(dep=depValue)
    if (cpValue != ""):
        TCommunes.objects.filter(id_commune=idCommuneValue).update(cp=cpValue)
    return HttpResponseRedirect("/home/ongletCommunes/"+idx)

# Create your views here.


'''def index(request):
    data_poids = TPoids.objects.all()
    context = {
        "Poids": data_poids,
    }
    return render(request, 'index.html', context)'''


def pagePoids(request, idx):
    idx = int(idx)
    t_min = (idx-1)*10
    t_max = (idx)*10
    taille = len(TPoids.objects.all())
    idx_max = math.ceil(taille/10)
    data_poids = TPoids.objects.all()[t_min:t_max]
    context = {
        "Poids": data_poids,
        "Index": idx,
        "Index_max": idx_max,
    }
    return render(request, 'poids.html', context)


def ajoutPoids(request, idx, valmin, valtimbre):
    ajoutPoids = TPoids(valmin=valmin, valtimbre=valtimbre)
    ajoutPoids.save()
    return HttpResponseRedirect("/pagePoids/"+idx)


def modifierPoids(request, idx, id, valmin, valtimbre):
    if (valmin != ""):
        TPoidsv.objects.filter(idpoids=id).update(valmin=valmin)
    if (valtimbre != ""):
        TPoidsv.objects.filter(idpoids=id).update(valtimbre=valtimbre)
    return HttpResponseRedirect("/pagePoids/"+idx)


def pagePoidsVignettes(request, idx):
    idx = int(idx)
    t_min = (idx-1)*10
    t_max = (idx)*10
    taille = len(TPoidsv.objects.all())
    idx_max = math.ceil(taille/10)
    data_poids = TPoidsv.objects.all()[t_min:t_max]
    context = {
        "Poids": data_poids,
        "Index": idx,
        "Index_max": idx_max,
    }
    return render(request, 'poidsVignettes.html', context)


def ajoutPoidsVignettes(request, idx, valmin, valtimbre):
    ajoutPoids = TPoidsv(valmin=valmin, valtimbre=valtimbre)
    ajoutPoids.save()
    return HttpResponseRedirect("/pagePoidsVignettes/"+idx)


def modifierPoidsVignettes(request, idx, id, valmin, valtimbre):
    if (valmin != ""):
        TPoidsv.objects.filter(idpoids=id).update(valmin=valmin)
    if (valtimbre != ""):
        TPoidsv.objects.filter(idpoids=id).update(valtimbre=valtimbre)
    return HttpResponseRedirect("/pagePoidsVignettes/"+idx)


def list(request):
    return render(
        request,
        template_name='liste_utilisateurs.html',
        context={'utilisateurs': TUtilisateur.objects.all().order_by('prenom_utilisateur', 'nom_utilisateur')})


def toggle_active(request, id: int):

    # if request.POST.get('toggle_active'):
    utilisateur = TUtilisateur.objects.get(pk=id)
    utilisateur.is_active = not utilisateur.is_active
    utilisateur.save()

    return list(request)


def add(request):

    if request.POST:
        TUtilisateurForm(request.POST).save()
        return list(request)
    else:
        form = TUtilisateurForm()

    return render(
        request,
        template_name='ajout_utilisateur.html',
        context={'form': form})


def change(request, id: int):

    if request.POST:
        TUtilisateurForm(request.POST, TUtilisateur.objects.get(pk=id)).save()
        return list(request)
    else:
        form = TUtilisateurForm(TUtilisateur.objects.get(pk=id))

    return render(
        request,
        template_name='change_utilisateur.html',
        context={'form': form, 'id': id})
