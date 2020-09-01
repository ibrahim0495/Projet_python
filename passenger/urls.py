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
    path('driver/profile', views.landing_diver, name='driver'),
    path('driver/ajout_trajet', views.ajouter_trajet, name='form_ajout_trajet'),
    path('driver/modifier', views.trajet_modifier, name='form_modif_trajet'),
    path('driver/modif_trajet', views.modifier_trajet, name='form_modif_trajet'),
    path('driver/liste_driver', views.list_driver, name='driver_list'),
    path('passenger/base',views.load_passenger, name='accueil_passenger'),
    path('passenger/souscrire',views.trajet_souscrite, name='souscrire_trajet')

]