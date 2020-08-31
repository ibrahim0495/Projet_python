from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import render, redirect

'''End Of Import'''
# ---------------------------------------------------------------------#


urlpatterns = [
    #################################################################################################################################################################################
    # URL FOR  LANDING-PAGE
    #################################################################################################################################################################################

    # LANDING Page url!

    # This is the landing-page url pattern having the ( ^ )-sign at the start means nothing comes before the defined url which will make it the index page##

    path('', views.landing, name='landing'),
    path('passenger/base',views.load_passenger, name='accueil_passenger'),
    path('passenger/souscrire',views.trajet_souscrite, name='souscrire_trajet')

]