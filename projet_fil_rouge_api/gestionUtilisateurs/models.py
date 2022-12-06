from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser

class TRole(models.Model):
    code_role = models.AutoField(primary_key=True)
    lib_role = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 't_role'



class TUtilisateur(AbstractBaseUser,models.Model):
    code_utilisateur = models.AutoField(primary_key=True)
    nom_utilisateur = models.CharField(max_length=50, blank=True, null=True)
    prenom_utilisateur = models.CharField(max_length=50, blank=True, null=True)
    couleur_fond_utilisateur = models.IntegerField(blank=True, null=True)
    date_cde_utilisateur = models.DateTimeField(blank=True, null=True)
    code_role = models.ForeignKey(TRole, models.DO_NOTHING, db_column='code_role', blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=128)
    is_superuser = models.IntegerField()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        managed = False
        db_table = 't_utilisateur'
        

    