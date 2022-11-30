from django.db import models

class TRole(models.Model):
    code_role = models.AutoField(primary_key=True)
    lib_role = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 't_role'
        
class TUtilisateur(models.Model):
    code_utilisateur = models.AutoField(primary_key=True)
    nom_utilisateur = models.CharField(max_length=50, blank=True, null=True)
    prenom_utilisateur = models.CharField(max_length=50, blank=True, null=True)
    couleur_fond_utilisateur = models.IntegerField(blank=True, null=True)
    date_cde_utilisateur = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    code_role = models.ForeignKey(TRole, models.DO_NOTHING, db_column='code_role', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_utilisateur'
        

    