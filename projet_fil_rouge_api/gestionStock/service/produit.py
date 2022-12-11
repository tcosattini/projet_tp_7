from django.core import serializers
from authentification.models import TObjet


def getAll():
  """_summary_

  Returns:
      _type_: _description_
  """

  try:
    response = []
    serializers.deserialize("json", TObjet.objects.all())
    for obj in TObjet.objects.all():
      response.append(obj)
    return {"response": response}
  except:
    return {'produits non trouvés'}


def create(validateObject):
  """_summary_

  Args:
      validateObject (_type_): _description_

  Returns:
      _type_: _description_
  """

  try:
    newProduit = TObjet.objects.create(**validateObject.dict())
    return {"nouveau produit": newProduit}
  except:
    return {'impossible de créer ce produit'}


def update(codobj, validateObject):
  """_summary_

  Args:
      codobj (_type_): _description_
      validateObject (_type_): _description_

  Returns:
      _type_: _description_
  """

  try:
    # Lever exception si produit non trouvé
    selectedProduit = TObjet.objects.filter(
        codobj=codobj).update(**validateObject.dict())
    return {"produit modifié avec succés": selectedProduit}
  except:
    return {'impossible de modifier ce produit'}


def delete(codobj):
  try:
    # Lever exception si produit non trouvé
    selectedProduit = TObjet.objects.filter(codobj=codobj).delete()
    return {"produit supprimé avec succés": selectedProduit}
  except:
    return {'impossible de supprimer ce produit'}
