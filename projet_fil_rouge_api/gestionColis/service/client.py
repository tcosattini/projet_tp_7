from authentification.models import TClient
from django.core import serializers
from fastapi import HTTPException


def getAll():
  """_summary_

  Returns:
      _type_: _description_
  """

  try:
    response = []
    serializers.deserialize("json", TClient.objects.all())
    for obj in TClient.objects.all():
      response.append(obj)
    return {"response": response}
  except:
    return {'clients non trouvés'}


def create(validateObject):
  """_summary_

  Args:
      validateObject (_type_): _description_

  Raises:
      HTTPException: _description_

  Returns:
      _type_: _description_
  """

  try:
    newClient = TClient.objects.create(**validateObject.dict())
    print(newClient)
    return {"nouveau client": newClient}
  except:
    raise HTTPException(
        status_code=426, detail="Impossible de créer ce client")


def update(codcli, validateObject):
  """_summary_

  Args:
      codcli (_type_): _description_
      validateObject (_type_): _description_

  Raises:
      HTTPException: _description_

  Returns:
      _type_: _description_
  """

  try:
    findSelectedClient = TClient.objects.get(codcli=codcli)
    selectedCommande = TClient.objects.filter(
        codcli=codcli).update(**validateObject.dict())
    selectedClient = TClient.objects.filter(
        codcli=codcli).update(**validateObject.dict())
    print(selectedClient)
    return {"client modifié avec succés"}
  except:
    raise HTTPException(status_code=404, detail="Commande non trouvée")


def delete(codcli):
  """_summary_

  Args:
      codcli (_type_): _description_

  Raises:
      HTTPException: _description_

  Returns:
      _type_: _description_
  """

  try:
    findSelectedClient = TClient.objects.get(codcli=codcli)
    selectedClient = TClient.objects.filter(codcli=codcli).delete()
    print(selectedClient)
    return {"client supprimé avec succés"}
  except:
    raise HTTPException(status_code=404, detail="Commande non trouvée")
