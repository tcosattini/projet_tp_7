from typing import Optional
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models


# @login_required(login_url='auth/login')
def add(request):
    return render(request, template_name='ajout_utilisateur.html')


# @login_required(login_url='auth/login')
def list(request):

    if request.POST.get('toggle_utilisateur'):
        pass

    return render(
        request,
        template_name='liste_utilisateurs.html',
        context={'utilisateurs': models.TUtilisateur.objects.all().order_by('prenom_utilisateur', 'nom_utilisateur')})


def toggle_active(request, id: int):

    if request.POST.get('toggle_active'):
        utilisateur = models.TUtilisateur.objects.get(pk=id)
        utilisateur.is_active = not utilisateur.is_active
        utilisateur.save()

    return list(request)


def change(request, id: int):

    if id:
        return render(
            request,
            template_name='liste_utilisateurs.html',
            context={'changed': False})

    return list(request)


"""methode used to redirect user to home pae of the module
"""


def home(request):
    return redirect('list/', permanent=False)
