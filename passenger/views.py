from django.shortcuts import render,redirect

from django.conf import settings

from django.http import HttpResponse

from django.conf.urls.static import static

from . import models

from django.contrib.auth.models import User


from django.contrib.auth.decorators import login_required
'''
The @login_required declarator limits access of view function to only 
authenticated users
'''
#---------------------------------------------------------------------#
'''End Of Import'''
#---------------------------------------------------------------------#

# VIEW FUNCTIONS HERE!


#################################################################################################################################################################################
#LANDING PAGE VIEW FUNCTION
#################################################################################################################################################################################

#Login page view function
def landing(request):
    return render(request,'landingpage/land-page.html')
