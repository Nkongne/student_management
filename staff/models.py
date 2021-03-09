from django.db import models

class Personnel(models.Model):
    nom=models.CharField(max_length=100)
    tel=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

    POSTE=[('Enseignant','Enseignant'),
                   ('Surveillant','Surveillant'),
                   ('Censeur','Censeur'),
                   ('Proviseur','Proviseur')]
    fonction=models.CharField(max_length=50,choices=POSTE)

    def __str__(self):
        return self.nom

    #def __str__(self):
    # return self.POSTE

# Create your models here.
class EnseignantManager(models.Model):
    def get_queryset(self):
        return super(EnseignantManager, self).get_queryset().filter(fonction='Enseignant')
class Enseignant(Personnel):
    object=EnseignantManager()

class Meta:
    proxy=True

class SurveillantManager(models.Model):
    def get_queryset(self):
        return super(SurveillantManager, self).get_queryset().filter(fonction='Surveillant')
class Surveillant(Personnel):
    object=SurveillantManager()
class Meta:
    proxy=True

class CenseurManager(models.Model):
    def get_queryset(self):
        return super(CenseurManager, self).get_queryset().filter(fonction='Censeur')
class Censeur(Personnel):
    object=CenseurManager()
class Meta:
    proxy=True

class ProviseurManager(models.Model):
    def get_queryset(self):
        return super(ProviseurManager, self).get_queryset().filter(fonction='Proviseur')
class Proviseur(Personnel):
    object=ProviseurManager()
class Meta:
    proxy=True
