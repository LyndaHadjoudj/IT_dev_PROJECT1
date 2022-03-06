from django.db import models

# Create your models here.
class Membre (models.Model):
    NomM = models.CharField(max_length=20)
    PrenomM = models.CharField(max_length=20)

class Reunion (models.Model):
    DateR =models.DateField(null=True)
    HeureR = models.TimeField()
    ButR =  models.CharField(max_length=200)
    DecisionR = models.CharField(max_length=200)
    TacheR = models.CharField(max_length=200)
    id_Membre=models.ForeignKey("Membre",on_delete=models.SET_NULL,null=True,blank=True)
    
class Avoir (models.Model):
    id_Membre=models.ForeignKey("Membre",on_delete=models.SET_NULL,null=True)
    id_Reunion =models.ForeignKey("Reunion",on_delete=models.SET_NULL,null=True)
    