from django import forms
from . import models


class Utilisateur(forms.Form):
    nom_utilisateur = forms.CharField()
    prenom_utilisateur = forms.CharField()
    couleur_fond_utilisateur = forms.IntegerField()
    code_role = forms.ChoiceField()
    username = forms.CharField()
    password = forms.CharField()
    is_superuser = forms.BooleanField()
