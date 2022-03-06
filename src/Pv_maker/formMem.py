from cProfile import label
from django.forms import ModelForm
from django import forms 
from .models import Avoir 


class AvoirForm (ModelForm):
    class Meta :
        model=Avoir
        fields='__all__'

        widgets={
            'idMembre' :forms.TextInput(attrs={'class':'form-control'}),
            'idReunion':forms.TextInput(attrs={'class':'form-control'}),
        }

        labels={
            'id_Membre':'indentificateur du membre',
            'id_Reunion':'indentificateur de la réunion',
        }
      