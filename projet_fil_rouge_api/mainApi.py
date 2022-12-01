from fastapi import FastAPI
from gestionStock.schema import *
from gestionStock.router import produitRouter
from gestionColis.router import clientRouter, commandeRouter


app = FastAPI()

app.include_router(produitRouter.router)
app.include_router(clientRouter.router)
app.include_router(commandeRouter.router)
