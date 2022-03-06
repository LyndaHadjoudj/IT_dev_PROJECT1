
from tkinter.ttk import Style
from django.forms import ModelForm
from django import forms 
from .models import Reunion 


class Reunion1Form (ModelForm):
    class Meta :
        model=Reunion
        fields=('ButR','DateR','HeureR','TacheR')
        
        widgets={
            'ButR':forms.TextInput(attrs={'class':'input input0','placeholder':'But de la reunion'}),
            'DateR':forms.DateInput(attrs={'class':'input input1 HideInput','placeholder':'Date de la reunion'}),
            'HeureR':forms.TextInput(attrs={'class':'input input1 HideInput','placeholder':'Heure de la reunion'}),
            'TacheR':forms.TextInput(attrs={'class':'input input2 HideInput' ,'placeholder':'Tache de la reunion'}),
        }
        labels={
               'ButR':'',
               'HeureR':'',
               'TacheR':'',
               'DateR':'',

         }