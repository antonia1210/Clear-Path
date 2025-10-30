from django.db import models
from datetime import date
# Create your models here.

class Item(models.Model):
    CHOICES = [
        ('Agricole', 'Agricole'),
        ('Ajutoare credinciosi', 'Ajutoare credinciosi'),
        ('Alte cheltuieli', 'Alte cheltuieli'),
        ('Alte venituri', 'Alte venituri'),
        ('Apa', 'Apa'),
        ('Asigurari', 'Asigurari'),
        ('Auto', 'Auto'),
        ('Birotica curatenie', 'Birotica curatenie'),
        ('Calendare', 'Calendare'),
        ('Capela', 'Capela'),
        ('Chirie', 'Chirie'),
        ('Colecta', 'Colecta'),
        ('Colportaj', 'Colportaj'),
        ('Combustibil', 'Combustibil'),
        ('Comision', 'Comision'),
        ('Consumabile', 'Consumabile'),
        ('Contribuții oficiale', 'Contribuții oficiale'),
        ('Cult', 'Cult'),
        ('Cutia Milei', 'Cutia Milei'),
        ('Deplasări', 'Deplasări'),
        ('Depuneri', 'Depuneri numerar'),
        ('Dobândă', 'Dobândă'),
        ('Donație', 'Donație'),
        ('Energie electrica', 'Energie electrica'),
        ('Exercitare cult', 'Exercitare cult'),
        ('Fcm', 'Fcm'),
        ('Imobilizari', 'Imobilizari'),
        ('Impozite/taxe', 'Impozite/taxe'),
        ('Incalzire','Incalzire'),
        ('Investitii', 'Investitii'),
        ('Loc de veci', 'Loc de veci'),
        ('Lumanari', 'Lumanari'),
        ('Obiecte cult', 'Obiecte cult'),
        ('Obiecte inventar', 'Obiecte inventar'),
        ('Parohii sarace', 'Parohii sarace'),
        ('Pictura', 'Pictura'),
        ('Posta telecomunicatii', 'Posta telecomunicatii'),
        ('Reparatii', 'Reparatii'),
        ('Rest Lumanari', 'Rest Lumanari'),
        ('Ridicari numerar', 'Ridicari numerar'),
        ('Salarii D112', 'Salarii D112'),
        ('Salarii fonduri proprii', 'Salarii fonduri proprii'),
        ('Salubritate', 'Salubritate'),
        ('Scaune', 'Scaune'),
        ('Servicii religioase', 'Servicii religioase'),
        ('Servicii terti', 'Servicii terti'),
        ('Sponsorizari', 'Sponsorizari'),
        ('Subventii', 'Subventii'),
        ('Tas', 'Tas'),
        ('Taxa cimitir', 'Taxa cimitir'),
        ('Utilaje', 'Utilaje'),
    ]
    CHOICES2 = [
        ('Încasare', 'Încasare'),
        ('Plată','Plată'),
    ]
    CHOICES3 = [
        ('Numerar', 'Numerar'),
        ('Card', 'Card'),
    ]
    numar_curent = models.IntegerField(default=1)
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