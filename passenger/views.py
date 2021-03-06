from django.shortcuts import render,redirect
from .models import Trajet,Personne,Passenger,Conducteur,Voyage
from django.forms import ModelForm,modelformset_factory
from .formulaire import TrajetsForm
from django.db import connection
#---------------------------------------------------------------------#
'''End Of Import'''
#---------------------------------------------------------------------#

# VIEW FUNCTIONS HERE!


#################################################################################################################################################################################
#LANDING PAGE VIEW FUNCTION
#################################################################################################################################################################################

def landing(request):
    return render(request,'landingpage/land-page.html')

def landing_accueil(request):
    dataTrajet = Trajet.objects.all()
    return render(request, 'landingpage/acceuil.html', {'dataTrajet': dataTrajet})

def landing_aPropos(request):
    return render(request, 'landingpage/a_propos.html')

def landing_diver(request):
    return render(request,'driver/home.html')

def ajouter_trajet(request):
    form= TrajetsForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TrajetsForm()
    dataTrajet=Trajet.objects.all()
    return render(request, 'driver/ajout_trajet.html',{'dataTrajet': dataTrajet,'form':form})



def modifier_trajet(request):
    id_trajet = int(str(request.GET['idT']))
    dataTrajet= Trajet.objects.get(id=id_trajet)
    return render(request, 'driver/modifier_trajet.html',{'dataTrajet':dataTrajet})

def trajet_modifier(request):
    if request.method == "POST":
        depart= str(request.POST['depart'])
        arrivee= str(request.POST['arrivee'])
        prix= str(request.POST['prix'])
        identifiant = int(str(request.POST['identifiant']))
        cursor = connection.cursor()
        cursor.execute('update passenger_trajet set depart= %s, arrivee= %s, prix= %s where id= %s',[depart,arrivee,prix,identifiant])
        cursor.fetchone()
        tjcursor = connection.cursor()
        tjcursor.execute('select passenger_personne.prenom,passenger_personne.nom,passenger_conducteur.nb_places,passenger_conducteur.id from passenger_personne join passenger_conducteur on passenger_personne.id=passenger_conducteur.id')
        result = tjcursor.fetchall()
        return render(request, 'driver/liste_driver.html', {'dataDriver': result})

def supprimer_trajet(request):
    id_trajet = int(str(request.GET['idT']))
    cursor = connection.cursor()
    cursor.execute('delete from passenger_trajet where id= %s',[id_trajet])
    cursor.fetchone()
    tjcursor = connection.cursor()
    tjcursor.execute('select passenger_personne.prenom,passenger_personne.nom,passenger_conducteur.nb_places,passenger_conducteur.id from passenger_personne join passenger_conducteur on passenger_personne.id=passenger_conducteur.id')
    result = tjcursor.fetchall()
    return render(request, 'driver/liste_driver.html', {'dataDriver': result})

def list_driver(request):
    cursor= connection.cursor()
    cursor.execute('select passenger_personne.prenom,passenger_personne.nom,passenger_conducteur.nb_places,passenger_conducteur.id from passenger_personne join passenger_conducteur on passenger_personne.id=passenger_conducteur.id')
    result= cursor.fetchall()
    return render(request,'driver/liste_driver.html',{'dataDriver':result})

def load_passenger(request):
    trajetFormSet = modelformset_factory(Trajet,fields=('depart','arrivee','prix'))
    formset = Trajet.objects.all()
    return render(request, 'passenger/base.html',{"formset":formset})

def trajet_souscrite(request):
    query = int(str(request.GET['query']))
    result = Trajet.objects.get(id=query)
    return render(request,'passenger/souscrire.html', {"result":result})
