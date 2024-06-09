from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from app import models
from app import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required
from .models import KonkurentuCenas
from django.contrib import messages


def sakums(request):
    return render(request, 'app/sakums.html')


def pakalpojuma_kartites(request):
    pakalpojuma_kartites = models.PakalpojumaKartiteGala.objects.all()
    return render(request, 'app/pakalpojuma_kartites.html', {'pakalpojuma_kartites': pakalpojuma_kartites})


def tirgus_cenu_izpete(request):
    return render(request, 'app/tirgus_cenu_izpete.html')


def mapping_tabula(request):
    maksas_vs_valsts = models.MappingTabula.objects.all().order_by('pak_kods')
    return render(request, 'app/mapping_tabula.html', {'maksas_vs_valsts': maksas_vs_valsts})

def list(request):
    visi_pakalpojumi = models.SettingsPskus230321.objects.filter(periods_lidz__gt=datetime.now()).order_by('manip_kods')
    return render(request, 'app/list.html', {'visi_pakalpojumi': visi_pakalpojumi})

def jauni_grozijumi(request):
    jauni_grozijumi = models.SettingsPskus230321.objects.all().order_by('auto_id')[:30][::-1]
    return render(request, 'app/list_jauni.html', {'jauni_grozijumi': jauni_grozijumi})

def izmaksu_detalizacija(request):
    izmaksu_detalizacija = models.SettingsPskus230321.objects.filter(periods_lidz__gt=datetime.now()).order_by('manip_kods')
    return render(request, 'app/izmaksu_detalizacija.html', {'izmaksu_detalizacija': izmaksu_detalizacija})

def konkurentu_cenas(request):
    konkurentu_cenas = models.KonkurentuCenas.objects.filter(speka_lidz__gt=datetime.now()).order_by('pakalpojuma_kods')
    return render(request, 'app/tirgus.html', {'konkurentu_cenas': konkurentu_cenas})


def jauna_forma_pakalpojumi(request):
    return render(request, 'app/jauna_forma_pakalpojumi.html')

def jauna_forma_konkurenti(request):
    return render(request, 'app/jauna_forma_konkurenti.html')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}")
                    return redirect('/')
                else:
                    messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "app/login.html",
                  context={"form":form})
    
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("sakums")

def nav_jauna_forma(request):
    return render(request, 'app/nav_jauna_forma.html')


def list_view(request):
    return render(request, 'app/list_view.html')


def insertrecord (request):
    if request.method == 'POST':
        form = forms.KonkurentiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        if request.POST.get('nozare') and request.POST.get('pakalpojuma_kods') and request.POST.get('pakalpojuma_nosaukums') and request.POST.get('konkurents_nosaukums') and request.POST.get('speka_no') and request.POST.get('speka_lidz') and request.POST.get('cena'):
            saverecord = KonkurentuCenas()
            saverecord.nozare=request.POST.get('nozare')
            saverecord.pakalpojuma_kods=request.POST.get('pakalpojuma_kods')
            saverecord.pakalpojuma_nosaukums=request.POST.get('pakalpojuma_nosaukums')
            saverecord.konkurents_nosaukums=request.POST.get('konkurents_nosaukums')
            saverecord.speka_no=request.POST.get('speka_no')
            saverecord.speka_lidz=request.POST.get('speka_lidz')
            saverecord.cena=request.POST.get('cena')
            saverecord.save()
            messages.success(request, 'record save')
            return render(request, 'index.html')

    else:
        form = forms.KonkurentiForm()
    
    return render(request, 'index.html', {'form': form})

def edit(request, pk, template_name='app/edit.html'):
    konkurents =  models.KonkurentuCenas.objects.get(gad_id= pk)
    if request.method == 'POST':
        form = forms.tirgusForm(request.POST, instance= konkurents)
        if form.is_valid():
            form.save()
            return redirect('tirgus')

    else:
        form = forms.tirgusForm(instance= konkurents)
    return render(request, 'app/edit.html', {'form':form})
    
def delete(request, pk, template_name='app/confirm-delete.html'):
    konkurents =  models.KonkurentuCenas.objects.get(gad_id= pk)
    if request.method=='POST':
        konkurents.delete()
        return redirect('tirgus')
    return render(request, 'app/confirm-delete.html', {'konkurents':konkurents})

#def detail_salidzinajums(request, pk):
 #   konkurents = models.CenuSalidzinajums.objects.get(pakalpojuma_id= pk)
 #   return render(request,'app/detail_salidzinajums.html', {'konkurents':konkurents})