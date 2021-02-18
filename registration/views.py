from __future__ import unicode_literals

from django.template.loader import render_to_string, get_template
from xhtml2pdf import pisa
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from  .form import registrationForm,creer_classeForm,creer_parentForm,payerForm,payerTrancheForm
from django.template import loader,Context
from .models import Eleve,Classe,Parent
from django.http import HttpResponse
import datetime
def home(request):
    return render(request, 'templates/home.html',context={'welcome'})
def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body>It is now %s.</body></html>" % now
    return  HttpResponse(html)
def listEleve(request,eleve_id ):
    return HttpResponse('you are looking at the results of eleves %s.' %eleve_id)
# Create your views here.
def index(request):
    eleves=Eleve.objects.all()
    t=loader.get_template('index.html')
    c={'eleve':Eleve}
    #context_dict=c.flatten()
    return  HttpResponse(render(request,'index.html',c))
def home_view(request):
    template=loader.get_template('index.html')
    response_body=template.render
    return  HttpResponse(response_body)
def eleve(request):
    from django.template import Template,Context
    object=Eleve.objects.all().order_by('nom')
    template=loader.get_template("eleves.html")
    print(str(template))
    c={'eleve':object}

    #print(str(template.render(context)))
    return HttpResponse(render(request,'eleves.html',c))
def classes(request):
    classes=Classe.objects.all().order_by('nom_classe')
    c={'classes':classes}

    return HttpResponse(render(request, 'classes.html', c))
def parents(request):
    parent=Parent.objects.all().order_by('nom')
    c={'parents':parent}

    return HttpResponse(render(request, 'parents.html', c))
def registration_detail_view(request):
    obj=Eleve.objects.get(id=7)
    context={
        'nom':obj.nom,
        'prenom':obj.prenom,
        'dateNaissance':obj.datenaiss,
        'lieuNaissance':obj.lieunaiss,
        'sex':obj.sex,
        'parents':obj.parent,
        'classe':obj.classe
    }
    return render(request,'registration/registration_detail.html',context)

def registration_create_view(request):
    form=registrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=registrationForm()



    context={
       'form':form
    }
    return render(request,'registration/registration_create.html',context)
def creer_classe_view(request):
    form=creer_classeForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=creer_classeForm
    context={
        'form':form
    }
    return render(request,'registration/creer_classe.html',context)
def creer_parent_view(request):
    form=creer_parentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=creer_parentForm
    context={
        'form':form
    }
    return render(request,'registration/creer_parent.html',context)
def liste_eleve_pdf(request):
    eleve=get_object_or_404(Eleve,id=10)
    response=HttpResponse(content_type="application/pdf")
    response["content-Disposition"]="attachement ;"\
        "filename=%$_%$.pdf" %(
        eleve.nom,
        eleve.prenom

    )
    html=render_to_string("registration/eleve/eleve_pdf.html",{
        "eleve":eleve,
        "MEDIA_ROOT":settings.MEDIA_ROOT,
        "STATIC_ROOT": settings.STATIC_ROOT,
    })
    pdf=pisa.pisaDocument(
        StringIO(html.encode("UTF-8")),
        response,
        encoding="UTF-8",

    )
    return response

def generate_PDF(request):
    all_eleves = Eleve.objects.all().order_by("nom")
    context = {
       'all_eleves':all_eleves
    }

    template = get_template('registration/eleve/eleve_pdf.html')
    html  = template.render(context)

    file = open('test.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
            encoding='utf-8')

    file.seek(0)
    pdf = file.read()
    file.close()
    return HttpResponse(pdf, 'application/pdf')
def payer_view(request):
    form = payerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = payerForm
    context = {
        'form': form
    }
    return render(request, 'registration/payer_frais.html', context)
def payer_tranche_view(request):
    form = payerTrancheForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = payerTrancheForm
    context = {
        'form': form
    }
    return render(request, 'registration/payer_tranche.html', context)
def eleve_view(request):
    context={}
    return render(request,'registration/eleve_detail.html',context)