from django.db import models

# Create your models here.

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
    id_commune = models.ForeignKey('TCommunes', models.DO_NOTHING, db_column='id_commune', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_client'

class TCommunes(models.Model):
    id_commune = models.AutoField(primary_key=True)
    dep = models.PositiveIntegerField(db_column='DEP', blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    communes = models.CharField(db_column='COMMUNES', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_communes'

class TDtlcode(models.Model):
    codcde = models.IntegerField(blank=True, null=True)
    codobj = models.ForeignKey('TObjet', models.DO_NOTHING, db_column='codobj', blank=True, null=True)
    qte = models.IntegerField(blank=True, null=True)
    colis = models.IntegerField(db_column='Colis', blank=True, null=True)  # Field name made lowercase.
    commentaire = models.CharField(db_column='Commentaire', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id_dtl_commande = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 't_dtlcode'        

class TEntcde(models.Model):
    codcde = models.AutoField(primary_key=True)
    datcde = models.DateTimeField(blank=True, null=True)
    codcli = models.ForeignKey(TClient, models.DO_NOTHING, db_column='codcli', blank=True, null=True)
    timbrecli = models.FloatField(blank=True, null=True)
    timbrecde = models.FloatField(blank=True, null=True)
    nbcolis = models.PositiveIntegerField(db_column='Nbcolis', blank=True, null=True)  # Field name made lowercase.
    cheqcli = models.FloatField(blank=True, null=True)
    idcondit = models.IntegerField(blank=True, null=True)
    cdecomt = models.TextField(db_column='cdeComt', blank=True, null=True)  # Field name made lowercase.
    barchive = models.IntegerField(blank=True, null=True)
    bstock = models.IntegerField(blank=True, null=True)
    id_dtl_commande = models.ForeignKey(TDtlcode, models.DO_NOTHING, db_column='id_dtl_commande', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_entcde'


class TObjet(models.Model):
    codobj = models.AutoField(primary_key=True)
    libobj = models.CharField(max_length=50, blank=True, null=True)
    tailleobj = models.CharField(db_column='Tailleobj', max_length=50, blank=True, null=True)  # Field name made lowercase.
    puobj = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    poidsobj = models.DecimalField(db_column='Poidsobj', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    indispobj = models.IntegerField(blank=True, null=True)
    o_imp = models.IntegerField(blank=True, null=True)
    o_aff = models.IntegerField(blank=True, null=True)
    o_cartp = models.IntegerField(blank=True, null=True)
    idcondit = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    o_ordre_aff = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_objet'