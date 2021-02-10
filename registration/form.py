from django import forms
from .models import Eleve,Parent,Classe,Frais_scolarite,Tranche
BIRTH_YEAR_CHOICES = ('1999', '2000', '2001')
GENDER_CHOICES = (('m', 'Male'), ('f', 'Female'))
FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
('green', 'Green'),
('black', 'Black'))
class creer_parentForm(forms.ModelForm):
    class Meta:
        model=Parent
        fields=[
            'nom',

            'tel',
            'adresse',
        ]
class creer_classeForm(forms.ModelForm):
    class Meta:
        model=Classe
        fields=[
            'nom_classe',
            'nbre_places',
        ]
class registrationForm(forms.ModelForm):
    class Meta:
        model=Eleve
        fields=[
            'nom',
            'prenom',
            'datenaiss',
            'lieunaiss',
            'sex',
            'classe',
            'parent',

        ]
class payerForm(forms.ModelForm):
    class Meta:
        model=Frais_scolarite
        fields=[
            'eleve',
            'classe',
            'montant_scolarite'
        ]
class payerTrancheForm(forms.ModelForm):
    class Meta:
        model=Tranche
        fields=[
            'numero',
            'montant_tranche',
            'totalite',
        ]