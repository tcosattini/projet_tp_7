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
  """_summary_

  Returns:
      _type_: _description_
  """

  return client.getAll()


@router.post("/", status_code=201)
def createClient(validateObject: Client):
  """_summary_

  Args:
      validateObject (Client): _description_

  Returns:
      _type_: _description_
  """

  return client.create(validateObject)


@router.put("/{codcli}")
def updateClient(validateObject: Client, codcli):
  """_summary_

  Args:
      validateObject (Client): _description_
      codcli (_type_): _description_

  Returns:
      _type_: _description_
  """

  return client.update(codcli, validateObject)


@router.delete("/{codecli}")
def deleteClient(codecli):
  """_summary_

  Args:
      codecli (_type_): _description_

  Returns:
      _type_: _description_
  """

  return client.delete(codecli)
