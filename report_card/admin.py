from django.contrib import admin

# Register your models here.
from .models import Discipline,Note,Examen
admin.site.register(Discipline)
admin.site.register(Note)
admin.site.register(Examen)
