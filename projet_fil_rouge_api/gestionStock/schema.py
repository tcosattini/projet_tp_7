from pydantic import BaseModel
from typing import Optional


class Produit(BaseModel):
  """_summary_

  Args:
      BaseModel (_type_): _description_
  """

  libobj: str
  tailleobj: Optional[str] = None
  puobj: Optional[int] = 0
  poidsobj: int
  indispobj: bool
  o_imp: int
  o_aff: Optional[str] = None
  o_cartp: Optional[int] = None
  idcondit: int
  points: int
  o_ordre_aff: int
  # is_active: bool
