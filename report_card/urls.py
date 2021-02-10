from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin
from report_card.views import remplir_note_view,ajouter_discipline_view
app_name="report_card"
urlpatterns=[
    path('note/', remplir_note_view,name='remplir_note'),
    path('discipline/',ajouter_discipline_view ,name='ajouter_discipine'),
    ]