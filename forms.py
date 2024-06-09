from datetime import date, timezone
import datetime
from project.settings import TIME_ZONE
from django import forms
from django.forms.widgets import DateInput, SelectDateWidget
from .models import KonkurentuCenas
import django.forms.utils
import django.forms.widgets


class KonkurentiForm(forms.Form):
    class Meta:
        model = KonkurentuCenas
    nozare = forms.TextInput()
    kods = forms.IntegerField()
    nosaukums = forms.TextInput()
    konkurents_nosaukums = forms.TextInput()
    speka_no = forms.DateField(widget=SelectDateWidget(), initial = date.today)
    speka_lidz = forms.DateField(widget=SelectDateWidget(None))
    cena = forms.FloatField()
    
    
regions_CHOICES =(
    ("1", "Australia and New Zealand"),
    ("2", "Baltic Countries"),
    ("3", "British Islands"),
    ("4", "Caribbean"),
    ("5", "Central Africa"),
    ("6", "Central America"),
    ("7", "Eastern Africa"),
    ("8", "Eastern Asia"),
    ("9", "Eastern Europe"),
    ("10", "Melanesia"),
    ("11", "Middle East"),
    ("12", "Nordic Countries"),
    ("13", "North America"),
)

class tirgusForm(forms.ModelForm):
    speka_no = forms.DateField(label= "Spēkā no")
    speka_lidz = forms.DateField(label= "Spēkā līdz")
    pakalpojuma_kods = forms.IntegerField(label= "Pakalpojuma kods")
    pakalpojuma_nosaukums = forms.CharField(label= "Pakalpojuma nosaukums")
    konkurents_nosaukums = forms.CharField(label= "Konkurents")
    cena = forms.FloatField(label= "Cena, EUR")
    koeficients = forms.IntegerField()
    nozare = forms.CharField(label= "Nozare")
    pilseta = forms.CharField(label= "Pilsēta")
    class Meta:
        model = KonkurentuCenas
        fields = ['speka_no', 'speka_lidz', 'pakalpojuma_kods', 'pakalpojuma_nosaukums', 'konkurents_nosaukums','cena', 'nozare', 'pilseta' ]
