


from typing import Union
from django.http import HttpResponse


def add():
    return {"detail":"addCommande"}

def update():
    return {"detail":"updateCommande"}

def getAll():
    return {"detail":"getCommandes"}

def getById():
    return {"detail":"getCommande"}