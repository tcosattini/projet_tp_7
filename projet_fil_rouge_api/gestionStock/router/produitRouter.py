from ..service import produit
from fastapi import FastAPI, APIRouter
from gestionStock.schema import *


router = APIRouter(
    prefix="/produit",
    tags=["produitRouter"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def getAllProduit():
  """_summary_

  Returns:
      _type_: _description_
  """

  return produit.getAll()


@router.post("/")
def createProduit(validateObject: Produit):
  """_summary_

  Args:
      validateObject (Produit): _description_

  Returns:
      _type_: _description_
  """

  return produit.create(validateObject)


@router.put("/{codobj}")
def updateProduit(validateObject: Produit, codobj):
  """_summary_

  Args:
      validateObject (Produit): _description_
      codobj (_type_): _description_

  Returns:
      _type_: _description_
  """

  return produit.update(codobj, validateObject)


@router.delete("/{codobj}")
def deleteProduit(codobj):
  """_summary_

  Args:
      codobj (_type_): _description_

  Returns:
      _type_: _description_
  """

  return produit.delete(codobj)
