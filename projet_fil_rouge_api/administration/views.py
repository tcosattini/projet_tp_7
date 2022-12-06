from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
import math

# Create your views here.

def index(request):
    data_poids = TPoids.objects.all()
    context = {
        "Poids": data_poids,
    }
    return render(request, 'index.html', context)


def pagePoids(request, idx):
    idx = int(idx)
    t_min = (idx-1)*10
    t_max = (idx)*10
    taille = len(TPoids.objects.all())
    idx_max = math.ceil(taille/10)
    data_poids = TPoids.objects.all()[t_min:t_max]
    context = {
        "Poids" : data_poids,
        "Index" : idx,
        "Index_max" : idx_max,
    }
    return render(request, 'poids.html', context)

def ajoutPoids(request, idx, valmin, valtimbre):
    ajoutPoids = TPoids(valmin = valmin, valtimbre = valtimbre)
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
        "Poids" : data_poids,
        "Index" : idx,
        "Index_max" : idx_max,
    }
    return render(request, 'poidsVignettes.html', context)

def ajoutPoidsVignettes(request, idx, valmin, valtimbre):
    ajoutPoids = TPoidsv(valmin = valmin, valtimbre = valtimbre)
    ajoutPoids.save()
    return HttpResponseRedirect("/pagePoidsVignettes/"+idx)

def modifierPoidsVignettes(request, idx, id, valmin, valtimbre):
    if (valmin != ""):
        TPoidsv.objects.filter(idpoids=id).update(valmin=valmin)
    if (valtimbre != ""):
        TPoidsv.objects.filter(idpoids=id).update(valtimbre=valtimbre)
    return HttpResponseRedirect("/pagePoidsVignettes/"+idx)