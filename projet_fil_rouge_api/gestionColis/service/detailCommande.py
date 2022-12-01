from ..models import TDtlcode
from django.core import serializers

def getAll():
 try:    
    response =[]
    serializers.deserialize("json", TDtlcode.objects.all())    
    for obj in TDtlcode.objects.all():
        response.append(obj)
    return {"response":response}    
 except: 
    return {'détails commandes non trouvées'}  

def create(validateObject):
 try:   
    newDetailCommande =  TDtlcode.objects.create(**validateObject.dict())
    return {"nouveau détail commande":newDetailCommande}
 except:
    return {'impossible de créer ce détail de commande'}

def update(id_dtl_commande,validateObject):
 try:
    # Lever exception si detail commande non trouvée
   findDetailCommande = TDtlcode.objects.get(id_dtl_commande=id_dtl_commande)
   selectedDetailCommande = TDtlcode.objects.filter(id_dtl_commande=id_dtl_commande).update(**validateObject.dict())
   findUpdatedCommande = TDtlcode.objects.get(id_dtl_commande=id_dtl_commande)
   return {"commande modifiée avec succés" : findUpdatedCommande}
 except:
    return {'impossible de modifier cette commande'}

def delete(id_dtl_commande):
 try:
    # Lever exception si detail  client non trouvé
   findDetailCommande = TDtlcode.objects.get(id_dtl_commande=id_dtl_commande)
   selectedCommande = TDtlcode.objects.filter(id_dtl_commande=id_dtl_commande).delete()
   return {"commande supprimée avec succés"}
 except:
    return {'impossible de supprimer cette commande'}
