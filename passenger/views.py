from django.shortcuts import render,redirect
from .models import Trajet,Personne,Passenger
from django.forms import ModelForm,modelformset_factory
from .formulaire import TrajetsForm

#---------------------------------------------------------------------#
'''End Of Import'''
#---------------------------------------------------------------------#

# VIEW FUNCTIONS HERE!


#################################################################################################################################################################################
#LANDING PAGE VIEW FUNCTION
#################################################################################################################################################################################

def landing(request):
    return render(request,'landingpage/land-page.html')

def landing_diver(request):
    return render(request,'driver/home.html')

def ajouter_trajet(request):
    if request.method == "POST":
        form= TrajetsForm(request.POST).save()
        return redirect('form_ajout_trajet')
    else:
        form = TrajetsForm()

    return render(request, 'driver/ajout_trajet.html', {'form':form, 'dataTrajet':Trajet.objects.all()})

def list_driver(request):
    return render(request,'driver_list',{'dataDriver'})

def load_passenger(request):
    trajetFormSet = modelformset_factory(Trajet,fields=('depart','arrivee','prix'))
    formset = trajetFormSet()
    return render(request, 'passenger/base.html',{"formset":formset})

def trajet_souscrite(request):
    obj = str(request.GET)
    query = request.GET['query']
    message = "{}".format(obj, query)
    dico={}
    dico[0]=message
    return render(request,'passenger/souscrire.html',dico)

