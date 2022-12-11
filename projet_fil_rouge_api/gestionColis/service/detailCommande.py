from authentification.models import TDtlcode
from django.core import serializers
from fastapi import HTTPException


def getAll():
  """_summary_

  Returns:
      _type_: _description_
  """

  try:
    response = []
    serializers.deserialize("json", TDtlcode.objects.all())
    for obj in TDtlcode.objects.all():
      response.append(obj)
    return {"response": response}
  except:
    return {'détails commandes non trouvées'}


def create(validateObject):
  """_summary_

  Args:
      validateObject (_type_): _description_

  Returns:
      _type_: _description_
  """

  try:
    newDetailCommande = TDtlcode.objects.create(**validateObject.dict())
    return {"nouveau détail commande": newDetailCommande}
  except:
    return {'impossible de créer ce détail de commande'}


def update(id_dtl_commande, validateObject):
  """_summary_

  Args:
      id_dtl_commande (_type_): _description_
      validateObject (_type_): _description_

  Raises:
      HTTPException: _description_

  Returns:
      _type_: _description_
  """

  try:
    findSelectedDetailCommande = TDtlcode.objects.get(
        id_dtl_commande=id_dtl_commande)
    selectedDetailCommande = TDtlcode.objects.filter(
        id_dtl_commande=id_dtl_commande).update(**validateObject.dict())
    findUpdatedCommande = TDtlcode.objects.get(
        id_dtl_commande=id_dtl_commande)
    return {"commande modifiée avec succés": findUpdatedCommande}
  except:
    raise HTTPException(status_code=404, detail="Commande non trouvée")


def delete(id_dtl_commande):
  """_summary_

  Args:
      id_dtl_commande (_type_): _description_

  Raises:
      HTTPException: _description_

  Returns:
      _type_: _description_
  """

  try:
    findSelectedDetailCommande = TDtlcode.objects.get(
        id_dtl_commande=id_dtl_commande)
    selectedCommande = TDtlcode.objects.filter(
        id_dtl_commande=id_dtl_commande).delete()
    return {"commande supprimée avec succés"}
  except:
    raise HTTPException(status_code=404, detail="Commande non trouvée")
