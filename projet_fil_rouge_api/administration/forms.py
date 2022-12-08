from dataclasses import field
from django import forms
from authentification.models import TUtilisateur


class TUtilisateurForm(forms.ModelForm):
    class Meta:
        model = TUtilisateur
        fields = ['nom_utilisateur', 'prenom_utilisateur',
                  'code_role', 'is_superuser', 'is_active']
