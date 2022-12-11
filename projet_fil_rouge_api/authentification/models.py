from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager


# app's models

class TClient(models.Model):
    codcli = models.AutoField(primary_key=True)
    genrecli = models.CharField(max_length=8, blank=True, null=True)
    nomcli = models.CharField(max_length=40)
    prenomcli = models.CharField(max_length=30, blank=True, null=True)
    adresse1cli = models.CharField(max_length=50, blank=True, null=True)
    adresse2cli = models.CharField(max_length=50, blank=True, null=True)
    adresse3cli = models.CharField(max_length=255, blank=True, null=True)
    cpcli = models.CharField(max_length=5, blank=True, null=True)
    villecli = models.CharField(max_length=50, blank=True, null=True)
    telcli = models.CharField(max_length=10, blank=True, null=True)
    emailcli = models.TextField(blank=True, null=True)
    portcli = models.CharField(max_length=10, blank=True, null=True)
    newsletter = models.IntegerField(blank=True, null=True)
    id_commune = models.ForeignKey(
        'TCommunes', models.DO_NOTHING, db_column='id_commune', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_client'


class TCommunes(models.Model):
    id_commune = models.AutoField(primary_key=True)
    # Field name made lowercase.
    dep = models.PositiveIntegerField(db_column='DEP', blank=True, null=True)
    # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    communes = models.CharField(
        db_column='COMMUNES', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_communes'
    
    def __str__(self):
        return self.communes


class TConditionnement(models.Model):
    idcondit = models.AutoField(primary_key=True)
    libcondit = models.CharField(max_length=50, blank=True, null=True)
    poidscondit = models.IntegerField(blank=True, null=True)
    prixcond = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    ordreimp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_conditionnement'


class TDept(models.Model):
    code_dept = models.CharField(primary_key=True, max_length=2)
    nom_dept = models.CharField(max_length=50, blank=True, null=True)
    ordre_aff_dept = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_dept'


class TDtlcode(models.Model):
    codcde = models.IntegerField(blank=True, null=True)
    codobj = models.ForeignKey(
        'TObjet', models.DO_NOTHING, db_column='codobj', blank=True, null=True)
    qte = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    colis = models.IntegerField(db_column='Colis', blank=True, null=True)
    # Field name made lowercase.
    commentaire = models.CharField(
        db_column='Commentaire', max_length=100, blank=True, null=True)
    id_dtl_commande = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 't_dtlcode'


class TEnseigne(models.Model):
    id_enseigne = models.AutoField(primary_key=True)
    lb_enseigne = models.CharField(max_length=50, blank=True, null=True)
    ville_enseigne = models.CharField(max_length=50, blank=True, null=True)
    dept_enseigne = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_enseigne'


class TEntcde(models.Model):
    codcde = models.AutoField(primary_key=True)
    datcde = models.DateTimeField(blank=True, null=True)
    codcli = models.ForeignKey(
        'TClient', models.DO_NOTHING, db_column='codcli', blank=True, null=True)
    timbrecli = models.FloatField(blank=True, null=True)
    timbrecde = models.FloatField(blank=True, null=True)
    # Field name made lowercase.
    nbcolis = models.PositiveIntegerField(
        db_column='Nbcolis', blank=True, null=True)
    cheqcli = models.FloatField(blank=True, null=True)
    idcondit = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    cdecomt = models.TextField(db_column='cdeComt', blank=True, null=True)
    barchive = models.IntegerField(blank=True, null=True)
    bstock = models.IntegerField(blank=True, null=True)
    id_dtl_commande = models.ForeignKey(
        'TDtlcode', models.DO_NOTHING, db_column='id_dtl_commande', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_entcde'


class TObjet(models.Model):
    codobj = models.AutoField(primary_key=True)
    libobj = models.CharField(max_length=50, blank=True, null=True)
    # Field name made lowercase.
    tailleobj = models.CharField(
        db_column='Tailleobj', max_length=50, blank=True, null=True)
    puobj = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    poidsobj = models.DecimalField(
        db_column='Poidsobj', max_digits=19, decimal_places=4, blank=True, null=True)
    indispobj = models.IntegerField(blank=True, null=True)
    o_imp = models.IntegerField(blank=True, null=True)
    o_aff = models.IntegerField(blank=True, null=True)
    o_cartp = models.IntegerField(blank=True, null=True)
    idcondit = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    o_ordre_aff = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        managed = True
        db_table = 't_objet'


class TPoids(models.Model):
    idpoids = models.AutoField(primary_key=True)
    valmin = models.FloatField()
    valtimbre = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_poids'


class TPoidsv(models.Model):
    idpoids = models.AutoField(primary_key=True)
    valmin = models.FloatField()
    valtimbre = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_poidsv'


class TRelCond(models.Model):
    idrelcond = models.AutoField(primary_key=True)
    codobj = models.ForeignKey(
        'TObjet', models.DO_NOTHING, db_column='codobj', blank=True, null=True)
    qteobjdeb = models.IntegerField(blank=True, null=True)
    qteobjfin = models.IntegerField(blank=True, null=True)
    codcond = models.ForeignKey(
        'TConditionnement', models.DO_NOTHING, db_column='codcond', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_rel_cond'


class TRole(models.Model):
    code_role = models.AutoField(primary_key=True)
    lib_role = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 't_role'

class TUtilisateur(AbstractBaseUser, models.Model):
    code_utilisateur = models.AutoField(primary_key=True)
    nom_utilisateur = models.CharField(max_length=50, blank=True, null=True)
    prenom_utilisateur = models.CharField(max_length=50, blank=True, null=True)
    couleur_fond_utilisateur = models.IntegerField(blank=True, null=True)
    date_cde_utilisateur = models.DateTimeField(blank=True, null=True)
    code_role = models.ForeignKey(
        'TRole', models.DO_NOTHING, db_column='code_role', blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=128)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        managed = True
        db_table = 't_utilisateur'
    
    def code(self):
        return self.code_utilisateur
    
    def nom(self):
        return self.nom_utilisateur
    
    def prenom(self):
        return self.prenom_utilisateur
    
    def coderole(self):
        return self.code_role
    
    def superuser(self):
        return self.is_superuser
    
    def active(self):
        return self.is_active
