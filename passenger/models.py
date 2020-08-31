from django.db import models


# Import User method for django
from django.contrib.auth.models import User

'''End Of Import'''


# ---------------------------------------------------------------------#


# MODELS CREATED HERE!

#################################################################################################################################################################################
# MODEL FOR PASSENGERS!
#################################################################################################################################################################################

# ...Class DRIVER added here...
class Personne(models.Model):
    prenom= models.CharField(max_length=200)
    nom= models.CharField(max_length=200)

    def __str__(self):
        return self.prenom + ' ' + self.nom

class Passenger(models.Model):
    # Attribute Variables for Driver class to represent different columns in database
    '''
    name-: This is the name of the passenger
    '''
    personne= models.ForeignKey(Personne,on_delete=models.CASCADE)

class Trajet(models.Model):
    depart= models.CharField(max_length=50)
    arrivee= models.CharField(max_length=50)
    prix= models.FloatField(max_length=10)

    def __str__(self):
        return self.depart + ' ' + self.arrivee+' '+str(self.prix)




#################################################################################################################################################################################
