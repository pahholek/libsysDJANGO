from django.db import models
import datetime
# Create your models here.


class book(models.Model):
    autor = models.CharField(max_length=200)
    data_wprowadzenia = models.DateTimeField(blank=True, null=True)
    isn = models.DecimalField(max_digits=100, decimal_places=0, blank=True, null=True)
    lokalizacja_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    nr_ubytku = models.DecimalField(max_digits=100, decimal_places=0, blank=True, null=True)
    opis = models.TextField(blank=True, null=True)
    powod_ubytkowania_id = models.TextField(blank=True, null=True)
    rok_wydania = models.DateField(blank=True, null=True)
    symbol_ukd = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    tematyka_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    tom = models.CharField(max_length=150, blank=True, null=True)
    typ_publikacji_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    tytul = models.CharField(max_length=350)
    wartosc = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True)
    wydawca = models.CharField(max_length=200, blank=True, null=True)
    id_czytelnika = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)