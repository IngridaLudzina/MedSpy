# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppKonkurentuCenuIevadeTabula(models.Model):
    id = models.BigAutoField(primary_key=True)
    konkurents_nodaukums = models.CharField(max_length=1000)
    cena = models.FloatField(blank=True, null=True)
    speka_no = models.DateField()

    class Meta:
        managed = False
        db_table = 'app_konkurentu_cenu_ievade_tabula'


class AppProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    bio = models.TextField()
    avatar = models.CharField(max_length=100)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_profile'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


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


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CenasIzmainas(models.Model):
    periods_pk = models.IntegerField()
    cena_private = models.FloatField()
    iep_periods_pk = models.IntegerField(blank=True, null=True)
    iep_cena = models.FloatField(blank=True, null=True)
    starpiba_eur = models.FloatField(db_column='starpiba_EUR', blank=True, null=True)  # Field name made lowercase.
    procenti = models.FloatField(blank=True, null=True)
    iep_cena2 = models.FloatField(blank=True, null=True)
    iep_cena3 = models.FloatField()

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cenas_izmainas'


class CenuSalidzinajums(models.Model):
    pakalpojuma_id = models.IntegerField()
    pskus = models.IntegerField(db_column='PSKUS')  # Field name made lowercase.
    pskus_cena = models.FloatField(db_column='PSKUS_cena')  # Field name made lowercase.
    valsts = models.IntegerField(blank=True, null=True)
    valsts_cena = models.FloatField(blank=True, null=True)
    konkurents = models.IntegerField(blank=True, null=True)
    tirgus_vid_cena = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cenu_salidzinajums'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


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


class IzmaksuPozicijas(models.Model):
    cena_id = models.IntegerField(primary_key=True)
    periods_pk = models.IntegerField()
    periods_no = models.DateField()
    periods_lidz = models.DateField()
    pakalpojuma_id = models.IntegerField()
    maksatajs_id = models.IntegerField()
    darba_samaksa = models.FloatField(blank=True, null=True)
    nodokli = models.FloatField(blank=True, null=True)
    med_preces = models.FloatField(blank=True, null=True)
    edinasana = models.FloatField(blank=True, null=True)
    saimn_izd = models.FloatField(blank=True, null=True)
    admin_izd = models.FloatField(blank=True, null=True)
    amortizacija = models.FloatField(blank=True, null=True)
    pelna = models.FloatField(blank=True, null=True)
    cena_private = models.FloatField()

    class Meta:
        managed = False
        db_table = 'izmaksu_pozicijas'


class IzmaksuPozicijasVisasGala(models.Model):
    periods_no = models.DateField()
    periods_lidz = models.DateField()
    maksatajs_nosaukums = models.CharField(max_length=45, db_collation='utf8_unicode_ci', blank=True, null=True)
    darba_samaksa = models.FloatField(blank=True, null=True)
    nodokli = models.FloatField(blank=True, null=True)
    med_preces = models.FloatField(blank=True, null=True)
    saimn_izd = models.FloatField(blank=True, null=True)
    admin_izd = models.FloatField(blank=True, null=True)
    amortizacija = models.FloatField(blank=True, null=True)
    cena_private = models.FloatField()

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'izmaksu_pozicijas_visas_gala'


class Konkurenti(models.Model):
    konkurents_id = models.AutoField(primary_key=True)
    konkurenta_nosaukums = models.CharField(max_length=45, blank=True, null=True)
    pilseta = models.CharField(max_length=45, blank=True, null=True)
    prioritate = models.IntegerField(blank=True, null=True)
    nozare_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'konkurenti'


class KonkurentuCenas(models.Model):
    gad_id = models.AutoField(primary_key=True)
    speka_no = models.DateField()
    speka_lidz = models.DateField()
    pakalpojuma_kods = models.IntegerField()
    pakalpojuma_nosaukums = models.TextField(db_collation='utf8_general_ci')
    konkurents_nosaukums = models.CharField(max_length=120, db_collation='utf8_general_ci')
    cena = models.FloatField()
    koeficients = models.IntegerField(blank=True, null=True)
    nozare = models.CharField(max_length=120, db_collation='utf8_general_ci', blank=True, null=True)
    pilseta = models.CharField(max_length=120, db_collation='utf8_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'konkurentu_cenas'


class KonkurentuCenasVideja(models.Model):
    periods_no = models.DateField()
    periods_lidz = models.DateField()
    pakalpojuma_id = models.IntegerField()
    cena_private = models.FloatField()

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'konkurentu_cenas_videja'


class KonkurentuCenasVisasGala(models.Model):
    speka_no = models.DateField()
    speka_lidz = models.DateField()
    pakalpojuma_id = models.IntegerField()
    pakalpojuma_nosaukums = models.CharField(max_length=1000, db_collation='utf8_unicode_ci', blank=True, null=True)
    konkurenta_nosaukums = models.CharField(max_length=45, db_collation='utf8_unicode_ci', blank=True, null=True)
    cena = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'konkurentu_cenas_visas_gala'


class Konkurentuinfo(models.Model):
    konkurenta_nosaukums = models.CharField(max_length=45, db_collation='utf8_unicode_ci', blank=True, null=True)
    pilseta = models.CharField(max_length=45, db_collation='utf8_unicode_ci', blank=True, null=True)
    nozare_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'konkurentuinfo'


class Maksatajs(models.Model):
    maksatajs_id = models.IntegerField(primary_key=True)
    maksatajs_veids = models.CharField(max_length=45)
    maksatajs_nosaukums = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'maksatajs'


class MappingTabula(models.Model):
    pak_kods = models.IntegerField(db_column='Pak_kods', primary_key=True)  # Field name made lowercase.
    pak_nosaukums = models.CharField(db_column='Pak_nosaukums', max_length=210, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    nozare = models.CharField(db_column='Nozare', max_length=84, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    atbilst_valsts_kods = models.IntegerField(db_column='Atbilst_valsts_kods', blank=True, null=True)  # Field name made lowercase.
    atbilst_valsts_nosaukums = models.CharField(db_column='Atbilst_valsts_nosaukums', max_length=870, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    vienojosais_maksas_kods = models.IntegerField(db_column='Vienojosais_maksas_kods', blank=True, null=True)  # Field name made lowercase.
    vid_tirgus_cena = models.FloatField(db_column='Vid_tirgus_cena', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapping_tabula'


class Nozare(models.Model):
    nozare_id = models.AutoField(primary_key=True)
    nosaukums = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'nozare'


class PakalpojumaKartiteGala(models.Model):
    periods_no = models.DateField(blank=True, null=True)
    periods_lidz = models.DateField(blank=True, null=True)
    pakalpojuma_id = models.IntegerField()
    pakalpojuma_nosaukums = models.CharField(max_length=1000, db_collation='utf8_unicode_ci')
    darba_samaksa = models.FloatField(blank=True, null=True)
    cena_private = models.FloatField(blank=True, null=True)
    maksatajs_id = models.IntegerField(blank=True, null=True)
    videja_cena = models.FloatField(blank=True, null=True)
    darba_alga_procentos = models.CharField(max_length=18, db_collation='utf8mb4_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'pakalpojuma_kartite_gala'


class Pakalpojums(models.Model):
    pakalpojuma_id = models.IntegerField(primary_key=True)
    pakalpojuma_nosaukums = models.CharField(max_length=1000)
    atb_valsts_kods = models.IntegerField(blank=True, null=True)
    nozare_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pakalpojums'


class ParPakalpojumiem(models.Model):
    pakalpojuma_id = models.IntegerField(db_column='Pakalpojuma_ID')  # Field name made lowercase.
    pakalpojuma_nosaukums = models.CharField(db_column='Pakalpojuma_nosaukums', max_length=1000, db_collation='utf8_unicode_ci')  # Field name made lowercase.
    nosaukums = models.CharField(db_column='Nosaukums', max_length=1000, db_collation='utf8_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    konkurenta_nosaukums = models.CharField(db_column='Konkurenta_nosaukums', max_length=45, db_collation='utf8_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    is_privately_paid = models.IntegerField(blank=True, null=True)
    cena_pec_maksataja = models.FloatField(blank=True, null=True)
    maksatajs_veids = models.CharField(max_length=45, db_collation='utf8_unicode_ci', blank=True, null=True)
    periods_no = models.DateField(db_column='Periods_no', blank=True, null=True)  # Field name made lowercase.
    periods_lidz = models.DateField(db_column='Periods_lidz', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'par_pakalpojumiem'


class ParPakalpojumiem1(models.Model):
    id = models.BigIntegerField()

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'par_pakalpojumiem1'


class ProfilesProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    bio = models.TextField()
    avatar = models.CharField(max_length=100)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profiles_profile'


class SettingsPskus230321(models.Model):
    auto_id = models.AutoField(primary_key=True)
    periods_no = models.DateField(blank=True, null=True)
    periods_lidz = models.DateField(blank=True, null=True)
    manip_kods = models.IntegerField(blank=True, null=True)
    manip_nosaukums = models.CharField(max_length=210, db_collation='utf8_general_ci', blank=True, null=True)
    darba_samaksa = models.FloatField(blank=True, null=True)
    valsts_soc_apdr_iemaksas = models.FloatField(blank=True, null=True)
    arstn_lidzekli = models.FloatField(blank=True, null=True)
    izd_pac_edin = models.FloatField(blank=True, null=True)
    saimn_izmaksas = models.FloatField(blank=True, null=True)
    admin_izd = models.FloatField(blank=True, null=True)
    amortiz = models.FloatField(blank=True, null=True)
    tarifs_euro = models.FloatField(blank=True, null=True)
    nozare = models.CharField(db_column='Nozare', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'settings_pskus_230321'


class TirgusCenaGala(models.Model):
    tirgus_cena_id = models.IntegerField(primary_key=True)
    pakalpojuma_id = models.IntegerField()
    konkurents_id = models.IntegerField()
    cena = models.FloatField(blank=True, null=True)
    speka_no = models.DateField()
    speka_lidz = models.DateField()

    class Meta:
        managed = False
        db_table = 'tirgus_cena_gala'


class UsersProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.CharField(max_length=100)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_profile'


class VisiPakalpojumi(models.Model):
    pakalpojuma_id = models.IntegerField(db_column='pakalpojuma_ID')  # Field name made lowercase.
    pakalpojuma_nosaukums = models.CharField(max_length=1000, db_collation='utf8_unicode_ci')
    atb_valsts_kods = models.IntegerField(blank=True, null=True)
    nozare_id = models.IntegerField(db_column='nozare_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'visi_pakalpojumi'
