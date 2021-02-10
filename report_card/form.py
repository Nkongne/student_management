from django import forms
from .models import Discipline,Note
class remplir_noteForm(forms.ModelForm):
    class Meta:
        model=Note


        fields=[

            'eleve',
            'discipline',
            'evaluation1',
            'evaluation2',
        ]

class ajouter_disciplineForm(forms.ModelForm):
    class Meta:
        model=Discipline


        fields=[

            'intitule',
            'coef',
            'enseignant',
            'classe',
        ]
