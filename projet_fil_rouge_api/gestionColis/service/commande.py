from ..models import TEntcde
from django.core import serializers

def getAll():
 try:    
    response =[]
    serializers.deserialize("json", TEntcde.objects.all())
    for obj in TEntcde.objects.all():
        response.append(obj)
    return {"response":response}
 except: 
    return {'commandes non trouvées'}  

def create(validateObject):
 try:   
    newCommande =  TEntcde.objects.create(**validateObject.dict())
    return {"nouvelle commande":newCommande}
 except:
    return {'impossible de créer cette commande'}

def update(codcde,validateObject):
 try:
    # Lever exception si detail commande non trouvée
   selectedCommande = TEntcde.objects.filter(codcde=codcde).update(**validateObject.dict())
   return {"commande modifiée avec succés"}
 except:
    return {'impossible de modifier cette commande'}

def delete(codcde):
 try:
    # Lever exception si client non trouvé
   selectedCommande = TEntcde.objects.filter(codcde=codcde).delete()
   return {"commande supprimée avec succés"}
 except:
    return {'impossible de supprimer cette commande'}
