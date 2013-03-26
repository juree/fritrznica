from django.db import models

# Create your models here.
class Bidders(models.Model):
    vpisna = models.CharField(max_length=8)
    ime = models.CharField(max_length=20)
    priimek = models.CharField(max_length=30)

class Offers(models.Model):
    bidders = models.ForeignKey(Bidders)
    vpisna = models.CharField(max_length=8)
    zeljeni_termin = models.CharField(max_length=30)
    predmet = models.CharField(max_length=30)

class Swaps(models.Model):
    vpisna1 = models.CharField(max_length=8)
    vpisna2 = models.CharField(max_length=8)
    predmet = models.CharField(max_length=30)
    termin1 = models.CharField(max_length=30)
    termin2 = models.CharField(max_length=30)