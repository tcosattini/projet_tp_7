from dataclasses import field
from django import forms
from authentification.models import TUtilisateur


class TUtilisateurForm(forms.ModelForm):
  """_summary_

  Args:
      forms (_type_): _description_
  """

  class Meta:
    model = TUtilisateur
    fields = ['nom_utilisateur', 'prenom_utilisateur',
              'code_role', 'is_superuser', 'is_active']
    labels = {
        'nom_utilisateur': ("Nom de l'utilisateur "),
        'prenom_utilisateur': ("Prénom de l'utilisateur "),
        'code_role': ("Rôle "),
        'is_superuser': ("L'utilisateur a le status de 'super-user' "),
        'is_active': ("L'utilisateur est actif "),
    }
