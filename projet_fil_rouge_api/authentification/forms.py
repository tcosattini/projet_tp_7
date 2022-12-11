from django import forms


class LoginForm(forms.Form):
  """_summary_

  Args:
      forms (_type_): _description_
  """

  username = forms.CharField(max_length=63, label='Nom d’utilisateur')
  password = forms.CharField(
      max_length=63, widget=forms.PasswordInput, label='Mot de passe')
