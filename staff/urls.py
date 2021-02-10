from django.contrib import admin
from django.conf.urls import url
from  django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import CreateView,DetailView
from django.views.generic.list import ListView
from staff.models import Enseignant,Personnel
from  .views import enseignantF,detail_enseignant
urlpatterns=[
    path ('enregistrer_enseignant/', CreateView.as_view(model=Enseignant, template_name="staff/enregistrer_enseignant.html", success_url = 'index'),name="enregistrer_enseignant"),
    path('liste_enseignant/',ListView.as_view(model=Personnel, template_name="staff/liste_enseignant.html"),name="liste_enseignant"),
    path ('enseignant_detail/',detail_enseignant, name="enseignant_detail"),
    path ('enseignant/', enseignantF, name="enseignant"),
    ]