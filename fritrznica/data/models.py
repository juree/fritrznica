from django.db import models
from django.contrib.auth.models import User

class Swaps(models.Model):
    predmet = models.CharField(max_length=30)
    termin1 = models.CharField(max_length=30)
    termin2 = models.CharField(max_length=30)
    #vpisna1 = models.CharField(max_length=8)
    #vpisna2 = models.CharField(max_length=8)

class Offers(models.Model):
    bidder = models.ForeignKey(User)
    swaps = models.ForeignKey(Swaps)
    #vpisna = models.CharField(max_length=8)
    termin = models.CharField(max_length=30)
    predmet = models.CharField(max_length=30)
    ucilnica = models.CharField(max_length=30)

class Bidders(models.Model):
    user = models.OneToOneField(User)
    vpisna = models.CharField(max_length=8)
    urnikVersion = models.CharField(max_length=9)