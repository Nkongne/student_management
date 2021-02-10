from django.shortcuts import render
from django.forms import ModelForm
from .models import Enseignant
from django.forms.fields import DateField, ChoiceField,MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

from django import forms
fonction=[('Enseignant','Enseignant'),
                   ('Surveillant','Surveillant'),
                   ('Censeur','Censeur'),
                   ('Proviseur','Proviseur')]
class EnseignantForm(forms.Form):
    nom=forms.CharField(max_length=30,label='Enter your name',initial='nom')
    tel=forms.CharField(max_length=20, label='Enter your phone number',initial='tel')
    email=forms.EmailField(max_length=30, label='Enter your Email address',initial='email')
    poste=forms.MultipleChoiceField(required=False,widget=CheckboxSelectMultiple,choices=fonction)
class EnseignantForm2(ModelForm):
    class Meta:
        model=Enseignant
        fields = [
            'nom',
            'tel',
            'email',
            'fonction',
        ]
