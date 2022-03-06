from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from django import forms 
from .models import Reunion 
class Reunion2Form (ModelForm):
    class Meta :
        model=Reunion
        fields=('DateR','HeureR')
        
        widgets={
            'DateR':forms.DateInput(attrs={'class':'input','placeholder':'Tapez ici'}),
            'HeureR':forms.TextInput(attrs={'class':'input','placeholder':'Tapez ici'}),
        }
        labels={
               'DateR':'',
                'HeureR':"",
         }