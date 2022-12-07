from ..models import TEntcde
from django.core import serializers
from fastapi import HTTPException
def getAll():
 try:    
    response =[]
    serializers.deserialize("json", TEntcde.objects.all())
    for obj in TEntcde.objects.all():
        response.append(obj)
    return {"response":response}
 except:
    raise HTTPException(status_code=404, detail="Commandes non trouvées")


def create(validateObject):
 try:   
    newCommande =  TEntcde.objects.create(**validateObject.dict())
    return {"nouvelle commande":newCommande}
 except:
    raise HTTPException(status_code=404, detail="Commandes non trouvées")


def update(codcde,validateObject):
 try:
    # Lever exception si detail commande non trouvée
   findSelectedCommande = TEntcde.objects.get(codcde=codcde)
   selectedCommande = TEntcde.objects.filter(codcde=codcde).update(**validateObject.dict())
   findUpdatedCommande = TEntcde.objects.get(codcde=codcde)
   return {"commande modifiée avec succés":findUpdatedCommande}
 except:
    raise HTTPException(status_code=404, detail="Commande non trouvée")


def delete(codcde):
 try:
   findSelectedDetailCommande = TEntcde.objects.get(codcde=codcde)
   selectedCommande = TEntcde.objects.filter(codcde=codcde).delete()
   return {"commande supprimée avec succés"}
 except:
    raise HTTPException(status_code=404, detail="Commande non trouvée")
