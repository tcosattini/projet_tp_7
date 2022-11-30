from django.shortcuts import render
from django.http import HttpResponse


def home(request, name):
    return HttpResponse('hello ' + name + ', welcome to the new world !')
