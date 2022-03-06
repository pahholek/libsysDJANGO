from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime
# Create your models here.

class user(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField()

class book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    publisher = models.CharField(max_length=300, blank=True, null=True)    
    ISBN = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    insert_date = models.DateField(blank=True, null=True)
    borrowed = models.BooleanField(default=False)
    borrowed_date = models.DateField(blank=True, null=True)
    borrowed_By = models.ForeignKey(user, blank=True, null=True, on_delete=models.SET_NULL)
    volume = models.IntegerField(blank=True, null=True)
    # autor = models.CharField(max_length=200)
    # data_wprowadzenia = models.DateTimeField(blank=True, null=True)
    # isn = models.DecimalField(max_digits=100, decimal_places=0, blank=True, null=True)
    # lokalizacja_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    # nr_ubytku = models.DecimalField(max_digits=100, decimal_places=0, blank=True, null=True)
    # opis = models.TextField(blank=True, null=True)
    # powod_ubytkowania_id = models.TextField(blank=True, null=True)
    # rok_wydania = models.DateField(blank=True, null=True)
    # symbol_ukd = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    # tematyka_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    # tom = models.CharField(max_length=150, blank=True, null=True)
    # typ_publikacji_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    # tytul = models.CharField(max_length=350)
    # wartosc = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True)
    # wydawca = models.CharField(max_length=200, blank=True, null=True)
    # id_czytelnika = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)


