from django import forms
from .models import Discipline,Note
from registration.models import Classe,Eleve
from staff.models import Enseignant
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
class BulletinForm(forms.Form):
    matiere=forms.ModelMultipleChoiceField(queryset=Discipline.objects.all(),widget=forms.CheckboxSelectMultiple)
    classe= forms.ModelMultipleChoiceField(queryset=Classe.objects.all(), widget=forms.CheckboxSelectMultiple)
    enseignant = forms.ModelMultipleChoiceField(queryset=Enseignant.objects.all(), widget=forms.CheckboxSelectMultiple)
    eleve = forms.ModelMultipleChoiceField(queryset=Eleve.objects.all(), widget=forms.CheckboxSelectMultiple)
    coef=forms.IntegerField(label='coefficient',initial='Coef',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Coef'
    }))
    note_I=forms.FloatField(label='note evaluation I',initial='note 1')
    note_II = forms.FloatField(label='note evaluation II', initial='note 2')
