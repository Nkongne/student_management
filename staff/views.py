from django.shortcuts import render
from .forms import EnseignantForm,EnseignantForm2
from  .models import Enseignant
# Create your views here.
def enseignantF(request):
    form = EnseignantForm2(request.POST or None)
    if form.is_valid():
        form.save()
        form = EnseignantForm2

    context = {
        'form': form
    }
    return render(request, 'staff/enseignantFo.html', context)
def detail_enseignant(request,cid):
    e=Enseignant.objects.get(pk=cid)
    context={'en':e}
    return render(request,'staff/detail.enseignant.html',context)
