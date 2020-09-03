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
    personne= models.ForeignKey(Personne,on_delete=models.CASCADE)


class Conducteur(models.Model):
    personne= models.ForeignKey(Personne,on_delete=models.CASCADE)
    nb_places = models.IntegerField()



class Trajet(models.Model):
    conducteur = models.ForeignKey(Conducteur, on_delete=models.CASCADE,default=1)
    depart= models.CharField(max_length=50)
    arrivee= models.CharField(max_length=50)
    prix= models.FloatField(max_length=10)


class Voyage(models.Model):
    trajet = models.ForeignKey(Trajet,on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger,on_delete=models.CASCADE,default=1)




#################################################################################################################################################################################
