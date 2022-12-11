from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentification.models import *
from .forms import *
import math


@login_required
def home(request):
  """ Page d'acceuil

  Args:
      request (_type_): _description_

  Returns:
      _type_: _description_
  """

  return render(request, template_name='home.html')


@login_required
def wip(request):
  """_summary_

  Args:
      request (_type_): _description_

  Returns:
      _type_: _description_
  """

  return render(request, template_name='WIP.html')

# Onglet "Objets" --- Madani ---


@login_required
def ongletObjets(request, idx):
  """_summary_

  Args:
      request (_type_): _description_
      idx (_type_): _description_

  Returns:
      _type_: _description_
  """

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


@login_required
def ajoutObjet(request, idx, nomValue, poidsValue, impValue, publicitaireValue, conditionnementValue, pointsValue):
  """_summary_

  Args:
      request (_type_): _description_
      idx (_type_): _description_
      nomValue (_type_): _description_
      poidsValue (_type_): _description_
      impValue (_type_): _description_
      publicitaireValue (_type_): _description_
      conditionnementValue (_type_): _description_
      pointsValue (_type_): _description_

  Returns:
      _type_: _description_
  """

  ajoutObjet = TObjet(libobj=nomValue, poidsobj=poidsValue, o_imp=impValue,
                      puobj=publicitaireValue, idcondit=conditionnementValue, points=pointsValue, is_active=1)
  ajoutObjet.save()
  return HttpResponseRedirect("/home/ongletObjets/"+idx)


@login_required
def modificationObjet(request, idx, idObjetValue, nomValue, poidsValue, impValue, publicitaireValue, conditionnementValue, pointsValue):
  """_summary_

  Args:
      request (_type_): _description_
      idx (_type_): _description_
      idObjetValue (_type_): _description_
      nomValue (_type_): _description_
      poidsValue (_type_): _description_
      impValue (_type_): _description_
      publicitaireValue (_type_): _description_
      conditionnementValue (_type_): _description_
      pointsValue (_type_): _description_

  Returns:
      _type_: _description_
  """

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


@login_required
def statusChangeObjet(request, idx, idObjetValue, statusValue):
  """_summary_

  Args:
      request (_type_): _description_
      idx (_type_): _description_
      idObjetValue (_type_): _description_
      statusValue (_type_): _description_

  Returns:
      _type_: _description_
  """

  TObjet.objects.filter(codobj=idObjetValue).update(is_active=statusValue)
  return HttpResponseRedirect("/home/ongletObjets/"+idx)


# Onglet "Emballages" --- Madani ---
@login_required
def ongletConditionnement(request, idx):
  """_summary_

  Args:
      request (_type_): _description_
      idx (_type_): _description_

  Returns:
      _type_: _description_
  """

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


@login_required
def ajoutConditionnement(request, idx, nomValue, poidsValue, tarifValue):
  """_summary_

  Args:
      request (_type_): _description_
      idx (_type_): _description_
      nomValue (_type_): _description_
      poidsValue (_type_): _description_
      tarifValue (_type_): _description_

  Returns:
      _type_: _description_
  """

  ajoutConditionnement = TConditionnement(
      libcondit=nomValue, poidscondit=poidsValue, prixcond=tarifValue)
  ajoutConditionnement.save()
  return HttpResponseRedirect("/home/ongletEmballages/"+idx)


@login_required
def modificationConditionnement(request, idx, idConditionnementValue, nomValue, poidsValue, tarifValue):
  """_summary_

  Args:
      request (_type_): _description_
      idx (_type_): _description_
      idConditionnementValue (_type_): _description_
      nomValue (_type_): _description_
      poidsValue (_type_): _description_
      tarifValue (_type_): _description_

  Returns:
      _type_: _description_
  """

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
@login_required
def ongletCommunes(request, idx):
  """_summary_

  Args:
      request (_type_): _description_
      idx (_type_): _description_

  Returns:
      _type_: _description_
  """

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


@login_required
def ajoutCommune(request, idx, communesValue, depValue, cpValue):
  """_summary_

  Args:
      request (_type_): _description_
      idx (_type_): _description_
      communesValue (_type_): _description_
      depValue (_type_): _description_
      cpValue (_type_): _description_

  Returns:
      _type_: _description_
  """

  ajoutCommune = TCommunes(dep=depValue, cp=cpValue, communes=communesValue)
  ajoutCommune.save()
  return HttpResponseRedirect("/home/ongletCommunes/"+idx)


@login_required
def modificationCommune(request, idx, idCommuneValue, communesValue, depValue, cpValue):
  """_summary_

  Args:
      request (_type_): _description_
      idx (_type_): _description_
      idCommuneValue (_type_): _description_
      communesValue (_type_): _description_
      depValue (_type_): _description_
      cpValue (_type_): _description_

  Returns:
      _type_: _description_
  """

  if (communesValue != ""):
    TCommunes.objects.filter(id_commune=idCommuneValue).update(
        communes=communesValue)
  if (depValue != ""):
    TCommunes.objects.filter(
        id_commune=idCommuneValue).update(dep=depValue)
  if (cpValue != ""):
    TCommunes.objects.filter(id_commune=idCommuneValue).update(cp=cpValue)
  return HttpResponseRedirect("/home/ongletCommunes/"+idx)


@login_required
def pagePoids(request, idx):
  """_summary_

  Args:
      request (_type_): _description_
      idx (_type_): _description_

  Returns:
      _type_: _description_
  """

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


@login_required
def ajoutPoids(request, idx, valmin, valtimbre):
  """_summary_

  Args:
      request (_type_): _description_
      idx (_type_): _description_
      valmin (_type_): _description_
      valtimbre (_type_): _description_

  Returns:
      _type_: _description_
  """

  ajoutPoids = TPoids(valmin=valmin, valtimbre=valtimbre)
  ajoutPoids.save()
  return HttpResponseRedirect("/home/pagePoids/"+idx)


@login_required
def modifierPoids(request, idx, id, valmin, valtimbre):
  """_summary_

  Args:
      request (_type_): _description_
      idx (_type_): _description_
      id (_type_): _description_
      valmin (_type_): _description_
      valtimbre (_type_): _description_

  Returns:
      _type_: _description_
  """

  if (valmin != ""):
    TPoids.objects.filter(idpoids=id).update(valmin=valmin)
  if (valtimbre != ""):
    TPoids.objects.filter(idpoids=id).update(valtimbre=valtimbre)
  return HttpResponseRedirect("/home/pagePoids/"+idx)


@login_required
def pagePoidsVignettes(request, idx):
  """_summary_

  Args:
      request (_type_): _description_
      idx (_type_): _description_

  Returns:
      _type_: _description_
  """

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


@login_required
def ajoutPoidsVignettes(request, idx, valmin, valtimbre):
  """_summary_

  Args:
      request (_type_): _description_
      idx (_type_): _description_
      valmin (_type_): _description_
      valtimbre (_type_): _description_

  Returns:
      _type_: _description_
  """

  ajoutPoids = TPoidsv(valmin=valmin, valtimbre=valtimbre)
  ajoutPoids.save()
  return HttpResponseRedirect("/home/pagePoidsVignettes/"+idx)


@login_required
def modifierPoidsVignettes(request, idx, id, valmin, valtimbre):
  """_summary_

  Args:
      request (_type_): _description_
      idx (_type_): _description_
      id (_type_): _description_
      valmin (_type_): _description_
      valtimbre (_type_): _description_

  Returns:
      _type_: _description_
  """

  if (valmin != ""):
    TPoidsv.objects.filter(idpoids=id).update(valmin=valmin)
  if (valtimbre != ""):
    TPoidsv.objects.filter(idpoids=id).update(valtimbre=valtimbre)
  return HttpResponseRedirect("/home/pagePoidsVignettes/"+idx)


@login_required
def list(request):
  """_summary_

  Args:
      request (_type_): _description_

  Returns:
      _type_: _description_
  """

  return render(
      request,
      template_name='liste_utilisateurs.html',
      context={'utilisateurs': TUtilisateur.objects.all().order_by('prenom_utilisateur', 'nom_utilisateur')})


@login_required
def toggle_active(request, id: int):
  """_summary_

  Args:
      request (_type_): _description_
      id (int): _description_

  Returns:
      _type_: _description_
  """

  # if request.POST.get('toggle_active'):
  utilisateur = TUtilisateur.objects.get(pk=id)
  utilisateur.is_active = not utilisateur.is_active
  utilisateur.save()

  return list(request)


@login_required
def add(request):
  """_summary_

  Args:
      request (_type_): _description_

  Returns:
      _type_: _description_
  """

  if request.POST:
    TUtilisateurForm(data=request.POST).save()
    return list(request)
  else:
    form = TUtilisateurForm()

  return render(
      request,
      template_name='ajout_utilisateur.html',
      context={'form': form})


@login_required
def change(request, id: int):
  """_summary_

  Args:
      request (_type_): _description_
      id (int): _description_

  Returns:
      _type_: _description_
  """

  if request.POST:
    TUtilisateurForm(data=request.POST, instance=TUtilisateur.objects.get(
        pk=id)).save(commit=True)
    return list(request)
  else:
    form = TUtilisateurForm(instance=TUtilisateur.objects.get(pk=id))

  return render(
      request,
      template_name='change_utilisateur.html',
      context={'form': form, 'id': id})
