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
    return commande.getAll()


@router.post("/", status_code=201)
def createCommande(validateObject: Commande):
    return commande.create(validateObject)


@router.put("/{codcde}")
def updateCommande(validateObject: Commande, codcde):
    return commande.update(codcde, validateObject)


@router.delete("/{codcde}")
def deleteCommande(codcde):
    return commande.delete(codcde)
