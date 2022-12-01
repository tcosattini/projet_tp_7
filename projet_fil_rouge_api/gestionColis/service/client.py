from ..models import TClient
from django.core import serializers


def getAll():
 try:    
    response =[]
    serializers.deserialize("json", TClient.objects.all())
    for obj in TClient.objects.all():
        response.append(obj)
    return {"response":response}
 except: 
    return {'clients non trouvés'}  

def create(validateObject):
 try:   
    newProduit =  TClient.objects.create(**validateObject.dict())
    return {"nouveau produit":newProduit}
 except:
    return {'impossible de créer ce client'}  

def update(codcli,validateObject):
 try:
    # Lever exception si client non trouvé
   selectedClient = TClient.objects.filter(codcli=codcli).update(**validateObject.dict())
   print(selectedClient)
   return {"client modifié avec succés"}
 except:
    return {'impossible de modifier ce client'}

def delete(codcli):
 try:
    # Lever exception si client non trouvé
   selectedClient = TClient.objects.filter(codcli=codcli).delete()
   print(selectedClient)
   return {"client supprimé avec succés"}
 except:
    return {'impossible de supprimer ce client'}
