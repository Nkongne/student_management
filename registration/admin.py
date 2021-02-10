from django.contrib import admin
from .models import Eleve
from .models import Parent
from .models import Classe,Frais_scolarite,Tranche
class EleveAdmin(admin.ModelAdmin):
    class EleveAdmin(admin.ModelAdmin):
        list_display=('nom','prenom','sex')
        read_only=('created_date')
admin.site.register(Eleve)
admin.site.register(Classe)
admin.site.register(Parent)
# Register your models here.
admin.site.register(Frais_scolarite)
admin.site.register(Tranche)