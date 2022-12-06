from typing import Optional
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models


def add(request):
    return render(request, template_name='ajout_utilisateur.html')


def list(request):

    return render(
        request,
        template_name='liste_utilisateurs.html',
        context={'utilisateurs': models.TUtilisateur.objects.all().order_by('prenom_utilisateur', 'nom_utilisateur')})


def toggle_active(request, id: int):

    # if request.POST.get('toggle_active'):
    utilisateur = models.TUtilisateur.objects.get(pk=id)
    utilisateur.is_active = not utilisateur.is_active
    utilisateur.save()

    return list(request)


def change(request, id: int):
    return render(
        request,
        template_name='change_utilisateur.html',
        context={'utilisateur': models.TUtilisateur.objects.get(pk=id)})


def save(request):

    if request.POST:
        pass

    form = None
    return render(
        request,
        template_name='liste_utilisateurs.html',
        context={'utilisateurs': models.TUtilisateur.objects.all()})


def home(request):
    return redirect('list/', permanent=False)
