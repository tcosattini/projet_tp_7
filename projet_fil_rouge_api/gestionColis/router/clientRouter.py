from ..service import client
from fastapi import APIRouter
from gestionColis.schema import *

router = APIRouter(
    prefix="/client",
    tags=["clientRouter"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def getAllClient():
   return client.getAll()

@router.post("/")
def createClient(validateObject: Client):
    return client.create(validateObject)
            
@router.put("/{codcli}")
def updateClient(validateObject: Client,codcli):
    return client.update(codcli,validateObject)

@router.delete("/{codecli}")
def deleteClient(codecli):
    return client.delete(codecli)
