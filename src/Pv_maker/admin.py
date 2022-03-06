from django.contrib import admin

from Pv_maker.models import Avoir
from Pv_maker.models import Membre
from Pv_maker.models import Reunion




admin.site.register(Membre)
admin.site.register(Reunion)
admin.site.register(Avoir)

# Register your models here.
