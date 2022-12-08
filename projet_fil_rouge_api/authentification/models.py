from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


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
        managed = False
        db_table = 't_client'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
        managed = False
        db_table = 't_communes'


class TConditionnement(models.Model):
    idcondit = models.AutoField(primary_key=True)
    libcondit = models.CharField(max_length=50, blank=True, null=True)
    poidscondit = models.IntegerField(blank=True, null=True)
    prixcond = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    ordreimp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_conditionnement'


class TDept(models.Model):
    code_dept = models.CharField(primary_key=True, max_length=2)
    nom_dept = models.CharField(max_length=50, blank=True, null=True)
    ordre_aff_dept = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
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
        managed = False
        db_table = 't_dtlcode'


class TEnseigne(models.Model):
    id_enseigne = models.AutoField(primary_key=True)
    lb_enseigne = models.CharField(max_length=50, blank=True, null=True)
    ville_enseigne = models.CharField(max_length=50, blank=True, null=True)
    dept_enseigne = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_enseigne'


class TEntcde(models.Model):
    codcde = models.AutoField(primary_key=True)
    datcde = models.DateTimeField(blank=True, null=True)
    codcli = models.ForeignKey(
        TClient, models.DO_NOTHING, db_column='codcli', blank=True, null=True)
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
        TDtlcode, models.DO_NOTHING, db_column='id_dtl_commande', blank=True, null=True)

    class Meta:
        managed = False
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

    class Meta:
        managed = False
        db_table = 't_objet'


class TPoids(models.Model):
    valmin = models.FloatField(primary_key=True)
    valtimbre = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_poids'


class TPoidsv(models.Model):
    valmin = models.FloatField(primary_key=True)
    valtimbre = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_poidsv'


class TRelCond(models.Model):
    idrelcond = models.AutoField(primary_key=True)
    codobj = models.ForeignKey(
        TObjet, models.DO_NOTHING, db_column='codobj', blank=True, null=True)
    qteobjdeb = models.IntegerField(blank=True, null=True)
    qteobjfin = models.IntegerField(blank=True, null=True)
    codcond = models.ForeignKey(
        TConditionnement, models.DO_NOTHING, db_column='codcond', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_rel_cond'


class TRole(models.Model):
    code_role = models.AutoField(primary_key=True)
    lib_role = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 't_role'


class TUtilisateur(AbstractBaseUser, models.Model):
    code_utilisateur = models.AutoField(primary_key=True)
    nom_utilisateur = models.CharField(max_length=50, blank=True, null=True)
    prenom_utilisateur = models.CharField(max_length=50, blank=True, null=True)
    couleur_fond_utilisateur = models.IntegerField(blank=True, null=True)
    date_cde_utilisateur = models.DateTimeField(blank=True, null=True)
    code_role = models.ForeignKey(
        TRole, models.DO_NOTHING, db_column='code_role', blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=128)
    is_superuser = models.BooleanField(blank=True, null=True, default=False)
    is_active = models.BooleanField(blank=True, null=True, default=True)
    last_login = models.DateField()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        managed = False
        db_table = 't_utilisateur'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(TUtilisateur, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(TUtilisateur, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(TUtilisateur, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'
