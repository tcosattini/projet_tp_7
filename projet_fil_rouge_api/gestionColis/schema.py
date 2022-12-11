from pydantic import BaseModel
from typing import Optional

class Client(BaseModel):
  """_summary_

  Args:
      BaseModel (_type_): _description_
  """  
  
  genrecli: str
  nomcli: str
  prenomcli : str
  adresse1cli : str
  adresse2cli : Optional[str] = None
  adresse3cli : Optional[str] = None
  villecli : str
  emailcli : str
  portcli : Optional[str] = None
  newsletter : Optional[bool] = None
  id_commune_id : Optional[int] = None

class Commande(BaseModel):
  """_summary_

  Args:
      BaseModel (_type_): _description_
  """  
  
  datcde: str
  codcli_id: int
  timbrecli : int
  timbrecde : int
  nbcolis : int
  cheqcli : int
  idcondit : Optional[int] = None
  cdecomt : Optional[int] = None
  barchive : Optional[int] = None
  bstock : bool
  id_dtl_commande_id : int

class DetailCommande(BaseModel):
  """_summary_

  Args:
      BaseModel (_type_): _description_
  """  
  
  codcde: int
  codobj_id: int
  qte: int
  colis: int
  commentaire: Optional[str] = None
  