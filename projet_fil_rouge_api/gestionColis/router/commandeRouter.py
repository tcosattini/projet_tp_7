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

@router.post("/",status_code=201)
def createCommande(validateObject: Commande):
    return commande.create(validateObject)
            
@router.put("/{codcde}")
def updateCommande(validateObject: Commande,codcde):
    return commande.update(codcde,validateObject)

@router.delete("/{codcde}")
def deleteCommande(codcde):
    return commande.delete(codcde)


@router.get("/detail")
def getAllCommande():
   return detailCommande.getAll()

@router.post("/detail",status_code=201)
def createCommande(validateObject: DetailCommande):
    return detailCommande.create(validateObject)
            
@router.put("/detail/{id_dtl_commande}")
def updateCommande(validateObject: DetailCommande,id_dtl_commande):
    return detailCommande.update(id_dtl_commande,validateObject)

@router.delete("/detail/{id_dtl_commande}")
def deleteCommande(id_dtl_commande):
    return detailCommande.delete(id_dtl_commande)