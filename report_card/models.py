from django.db import models
import datetime
from django.utils import timezone
from staff.models import Enseignant
from registration.models import Eleve,Classe

class Examen(models.Model):
    trimestre=models.CharField(max_length=50)
    annee=models.CharField(max_length=30)
    def __str__(self):
        self.trimestre


class Discipline(models.Model):
    intitule=models.CharField(max_length=50)
    coef=models.IntegerField(default=2)
    enseignant = models.ManyToManyField(Enseignant)
    classe=models.ManyToManyField(Classe)

    def __str__(self):
        return self.intitule


class Note(models.Model):
    evaluation1=models.FloatField(default=0)
    evaluation2 = models.FloatField(default=0)
    discipline=models.ManyToManyField(Discipline)
    eleve=models.ManyToManyField(Eleve)

    def __float__(self):
        return self.evaluation1







