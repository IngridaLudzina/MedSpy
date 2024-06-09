from django.db import models

# Create your models here.

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

class SettingsPskus230321(models.Model):
    periods_no = models.DateField(blank=True, null=True)
    periods_l_dz = models.DateField(blank=True, null=True)
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
        db_table = 'Settings_pskus_230321'

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

class PakalpojumaKartiteGala(models.Model):
    periods_no = models.DateField(blank=True, null=True)
    periods_lidz = models.DateField(blank=True, null=True)
    pakalpojuma_id = models.AutoField(primary_key=True)
    pakalpojuma_nosaukums = models.CharField(max_length=1000, db_collation='utf8_unicode_ci')
    darba_samaksa = models.FloatField(blank=True, null=True)
    cena_private = models.FloatField(blank=True, null=True)
    maksatajs_id = models.IntegerField(blank=True, null=True)
    videja_cena = models.FloatField(blank=True, null=True)
    darba_alga_procentos = models.CharField(max_length=18, db_collation='utf8mb4_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'pakalpojuma_kartite_gala'

class CenuSalidzinajums(models.Model):
    pakalpojuma_id = models.AutoField(primary_key=True)
    pskus = models.IntegerField(db_column='PSKUS')  # Field name made lowercase.
    pskus_cena = models.FloatField(db_column='PSKUS_cena')  # Field name made lowercase.
    valsts = models.IntegerField(blank=True, null=True)
    valsts_cena = models.FloatField(blank=True, null=True)
    konkurents = models.IntegerField(blank=True, null=True)
    tirgus_vid_cena = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'cenu_salidzinajums'