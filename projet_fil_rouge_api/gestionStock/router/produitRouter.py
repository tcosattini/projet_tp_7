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
   return produit.getAll()

@router.post("/")
def createProduit(validateObject: Produit):
    return produit.create(validateObject)
            
@router.put("/{codobj}")
def updateProduit(validateObject: Produit,codobj):
    return produit.update(codobj,validateObject)

@router.delete("/{codobj}")
def deleteProduit(codobj):
    return produit.delete(codobj)
