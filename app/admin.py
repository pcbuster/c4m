from django.contrib import admin
from app.models import Richiedente, Oggetto


admin.site.register(Richiedente)

class OggettoAdmin(admin.ModelAdmin):
    list_display = ('richiedente','idOggetto','titolo','prezzo',)
   # search_fields = ("idFornitore","ragioneSociale",'piva','nome','cognome')
    fieldsets = [
        ('Inserisci Oggetto',{
            'fields': ['richiedente', ]
        }),
        ('Oggetto', {
            'fields' : ['titolo', 'descrizione','prezzo',]
        }),
    ]

admin.site.register(Oggetto,OggettoAdmin)




