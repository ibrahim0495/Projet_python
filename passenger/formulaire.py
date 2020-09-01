from django.forms import ModelForm
from .models import Trajet

class TrajetsForm(ModelForm):
    class Meta:
        model= Trajet
        fields= ['depart','arrivee','prix']