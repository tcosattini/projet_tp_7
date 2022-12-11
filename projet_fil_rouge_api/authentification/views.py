from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from . import forms


def logout_user(request):
  """_summary_

  Args:
      request (_type_): _description_

  Returns:
      _type_: _description_
  """

  logout(request)
  return redirect('/')


def login_page(request):
  """_summary_

  Args:
      request (_type_): _description_

  Returns:
      _type_: _description_
  """

  form = forms.LoginForm()
  message = ''
  if request.POST:
    form = forms.LoginForm(request.POST)
    if form.is_valid():
      user = authenticate(
          username=form.cleaned_data['username'],
          password=form.cleaned_data['password'],
      )
      if user is not None:
        login(request, user)
        message = f'Bonjour, {user.get_username()}! Vous êtes connecté.'
        return redirect('/home')
      else:
        message = 'Identifiants invalides.'
  return render(
      request, 'login/login.html', context={'form': form, 'message': message})
