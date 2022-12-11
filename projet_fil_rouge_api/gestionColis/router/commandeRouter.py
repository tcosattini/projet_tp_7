from ..service import commande, detailCommande
from fastapi import APIRouter
from gestionColis.schema import *

router = APIRouter(
    prefix="/commande",
    tags=["commandeRouter"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def getAllCommande():
  """_summary_

  Returns:
      _type_: _description_
  """

  return commande.getAll()


@router.post("/", status_code=201)
def createCommande(validateObject: Commande):
  """_summary_

  Args:
      validateObject (Commande): _description_

  Returns:
      _type_: _description_
  """

  return commande.create(validateObject)


@router.put("/{codcde}")
def updateCommande(validateObject: Commande, codcde):
  """_summary_

  Args:
      validateObject (Commande): _description_
      codcde (_type_): _description_

  Returns:
      _type_: _description_
  """

  return commande.update(codcde, validateObject)


@router.delete("/{codcde}")
def deleteCommande(codcde):
  """_summary_

  Args:
      codcde (_type_): _description_

  Returns:
      _type_: _description_
  """

  return commande.delete(codcde)
