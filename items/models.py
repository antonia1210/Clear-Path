from django.db import models
from datetime import date
# Create your models here.

class Item(models.Model):
    CHOICES = [
        ('Neprecizat', 'Neprecizat'),
        ('Comision', 'Comision'),
        ('Consumabile', 'Consumabile'),
        ('Contribuții oficiale', 'Contribuții oficiale'),
        ('Cult', 'Cult'),
        ('Cutia Milei', 'Cutia Milei'),
        ('Deplasări', 'Deplasări'),
        ('Depuneri', 'Depuneri numerar'),
        ('Dobândă', 'Dobândă'),
        ('Donație', 'Donație'),
    ]
    CHOICES2 = [
        ('Încasare', 'Încasare'),
        ('Plată','Plată'),
    ]
    CHOICES3 = [
        ('Numerar', 'Numerar'),
        ('Card', 'Card'),
    ]
    data = models.DateField(default=date.today())
    document = models.IntegerField(default=1)
    denumire = models.CharField(max_length=200, blank = True)
    adresa = models.CharField(max_length=100, blank = True)
    explicatii = models.CharField(max_length=1000, blank = True)
    felul = models.CharField(max_length=100, choices=CHOICES, default='Neprecizat')
    tip = models.CharField(max_length=100, choices=CHOICES2, default='Încasare', blank = False)
    tip_incasare = models.CharField(max_length=100, choices=CHOICES3, default='Numerar', blank = False)
    pret = models.FloatField(default=0)
    church = models.ForeignKey('churches.Church', on_delete=models.CASCADE,related_name='items', blank=False, default=1)

    def __str__(self):
        return self.denumire