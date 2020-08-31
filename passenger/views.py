from django.shortcuts import render,redirect
from .models import Trajet,Personne,Passenger
from django.forms import ModelForm,modelformset_factory

#---------------------------------------------------------------------#
'''End Of Import'''
#---------------------------------------------------------------------#

# VIEW FUNCTIONS HERE!


#################################################################################################################################################################################
#LANDING PAGE VIEW FUNCTION
#################################################################################################################################################################################

def landing(request):
    return render(request,'landingpage/land-page.html')

def load_passenger(request):
    trajetFormSet = modelformset_factory(Trajet,fields=('depart','arrivee','prix'))
    formset = trajetFormSet()
    print(formset)
    return render(request, 'passenger/base.html',{"formset":formset})

def trajet_souscrite(request):
    obj = str(request.GET)
    query = request.GET['query']
    message = "{}".format(obj, query)
    dico={}
    dico[0]=message
    return render(request,'passenger/souscrire.html',dico)