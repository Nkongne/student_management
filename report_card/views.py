from __future__ import unicode_literals

from django.template.loader import render_to_string, get_template
from xhtml2pdf import pisa
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .form import remplir_noteForm,ajouter_disciplineForm,BulletinForm
from django.template import loader, Context
from registration.models import  Eleve, Classe
from django.http import HttpResponse
from django.contrib import messages
from .models import Note
from django.shortcuts import render

# Create your views here.
def remplir_note_view(request):
    form=remplir_noteForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=remplir_noteForm
        messages.add_message(request, messages.SUCCESS, 'Ces notes sont bien remplies et enregistrees')
    context={
       'form':form
    }

    return render(request,'report_card/remplir_note.html',context)


def ajouter_discipline_view(request):
    form=ajouter_disciplineForm(request.POST or None, initial={'classe':Classe.objects.all()[:1].get().id})
    if form.is_valid():
        form.save()
        form=ajouter_disciplineForm

    context={
       'form':form
    }
    return render(request,'report_card/ajouter_discipline.html',context)
def bulletin_view(request):
    form=BulletinForm(request.POST or None, initial={'eleve':Eleve.objects.all()[:1].get().id})
    if form.is_valid():
        form.save()
        form=BulletinForm
    context={
        "form":BulletinForm
    }
    return render(request, 'report_card/bulletin.html', context)
