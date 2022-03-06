from multiprocessing import context
from re import search
import re
from turtle import title
from django.shortcuts import render
from Pv_maker.form import Reunion1Form
from Pv_maker.formSuit import Reunion2Form
from Pv_maker.formMem import AvoirForm
from django.shortcuts import render, redirect
from .models import Reunion
from django.db.models import Q

# Create your views here.

def pageOne (request):
    return render(request,'index.html')

def pageTwo (request):
    if request.method == "POST":
         form = Reunion1Form(data=request.POST)
         if form.is_valid():
            form.save()
            print('Bien marcher')
            return redirect("Insc-etp3")

    else:
         formulaire =  Reunion1Form
         print('ca marche pas')
         return render(request,'page2.html',{"form": formulaire})




def pageFour(request):
     if request.method == "POST":
         form3 = AvoirForm(data=request.POST)
         if form3.is_valid():
            form3.save()
            return redirect("webone")
     else:
        formue2 = AvoirForm()
        print('ca marche pas')
        return render(request,'page4.html',{"formMem": formue2})

        
def pageFive(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(id__icontains=q) | Q(DateR__icontains=q) | Q(ButR__icontains=q) | Q(DecisionR__icontains=q) |  Q(HeureR__icontains=q))
        reuns= Reunion.objects.filter(multiple_q)
    else:
         reuns = Reunion.objects.all()
    context={
        'reuns':reuns
    }
    return render(request,'page5.html',{'reuns':reuns})

def have (request):
    reuns = Reunion.objects.all()
    return render(request,'page5.html',{' ':reuns})


