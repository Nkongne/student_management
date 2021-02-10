from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin
from registration.views import eleve,listEleve,classes,home,index,parents,registration_detail_view,registration_create_view,creer_classe_view,creer_parent_view,liste_eleve_pdf,generate_PDF,payer_view,payer_tranche_view
app_name="registration"
urlpatterns=[
    path("", index,name='acceuil'),
    path(r'classes/',classes, name='classes'),
    path('index/',index,name='index'),
    path('eleve/',eleve, name='eleves'),
    path('home/', home, name='home'),
    path('parents/',parents, name='parents'),
    path('detail/', registration_detail_view, name='detail'),
    path('creer_eleve/', registration_create_view, name='creer_eleve'),
    path('creer_parent/',creer_parent_view, name='creer_parent'),
    path('creer_classe/',creer_classe_view,name='creer_classe'),
    path('telecharger_liste_eleve/',liste_eleve_pdf,name='eleve_pdf'),
    path('telecharger/', generate_PDF, name='pdf'),
    path('payer_frais/',payer_view,name='payer_frais'),
    path('payer_tranche/',payer_tranche_view,name='payer_tranche')
]