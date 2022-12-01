from fastapi import FastAPI
from gestionStock.schema import *
from gestionStock import produitRouter

app = FastAPI()

app.include_router(produitRouter.router)
