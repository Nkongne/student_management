from django.db import models
import datetime
from django.utils import timezone
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple, SelectDateWidget

BIRTH_YEAR_CHOICES = ('1986','1987', '1988','1989', '1990','1991','1992','1993','1994', '1995','1996', '1997','1998','1999', '2000', '2001''2002', '2003','2004', '2005','2006', '2007')
GENDER_CHOICES = (('m', 'Male'), ('f', 'Female'))

class Parent(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    tel = models.CharField(max_length=50)

    def __str__(self):
        return self.nom



class Classe(models.Model):
    nom_classe = models.CharField(max_length=20)
    nbre_places = models.IntegerField(default=50)

    def __str__(self):
        return self.nom_classe


class Eleve(models.Model):

    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    datenaiss=models.DateTimeField('date de naissance:')
    lieunaiss=models.CharField('lieu de naissance:',max_length=50)
    sex=models.CharField(max_length=20)
    parent=models.ForeignKey(to=Parent,on_delete=models.CASCADE)
    classe = models.ForeignKey(to=Classe, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
class Frais_scolarite(models.Model):
    montant_scolarite=models.BigIntegerField(default=0)
    eleve = models.ForeignKey(to=Eleve, on_delete=models.CASCADE)
    classe = models.ForeignKey(to=Classe, on_delete=models.CASCADE)
    def __int__(self):
        self.montant_scolarite
class Tranche(models.Model):
    numero=models.CharField(max_length=30)
    montant_tranche=models.BigIntegerField(default=0)
    totalite = models.ForeignKey(to=Frais_scolarite, on_delete=models.CASCADE)
    def __str__(self):
        self.numero


# Create your models here.
