from django.db import models

class Richiedente(models.Model):
    idRichiedente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=True, blank=True)
    cognome = models.CharField(max_length=50, null=True, blank=True)
    regione = models.CharField(max_length=50, null=True, blank=True)
    citta = models.CharField(max_length=50, null=True, blank=True)
    indirizzo = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)
    Uomo = 'Uomo'
    Donna = 'Donna'
    scelta_sesso =(
        (Uomo, 'Uomo'),
        (Donna, 'Donna'),
    )
    sesso = models.CharField(max_length=5,choices=scelta_sesso, null=True, blank=True)
    foto = models.CharField(max_length=50, null=True, blank=True)
    valutazione = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{} ""{}".format(self.cognome, self.nome)

    class Meta:
        verbose_name = "Richiedente"
        verbose_name_plural = "Richiedenti"


class Oggetto(models.Model):
    idOggetto = models.AutoField(primary_key=True)
    richiedente = models.ForeignKey(Richiedente,on_delete=None,related_name='Oggetti')
    titolo = models.CharField(max_length=50, null=True, blank=True)
    regione = models.CharField(max_length=50, null=True, blank=True)
    citta = models.CharField(max_length=50, null=True, blank=True)
    descrizione = models.TextField(max_length=250, null=True, blank=True)
    DieciEuro = '10 Euro'
    VentiEuro = '20 EUro'
    TrentaEuro = '30 EUro'
    scelta_prezzo = (
        (DieciEuro, '10 Euro'),
        (VentiEuro, '20 Euro'),
        (TrentaEuro, '30 Euro'),
        )
    prezzo = models.CharField(max_length=10, choices=scelta_prezzo,null=True,blank=True)

    def __str__(self):
        return "{}" .format(self.titolo)

    def nome_cognome(richiedente):
        return '%s' % self.richiedente.nome

    def rich_nome(idRichiedente):
        return '%s %s' % (Richiedente.nome, Richiedente.cognome)

