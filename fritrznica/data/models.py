from django.db import models
from django.contrib.auth.models import User


class Swaps(models.Model):
    #not sure
    closed = models.NullBooleanField(default=True)


class Offers(models.Model):
    user = models.ForeignKey(User)
    termin = models.CharField(max_length=30)
    ucilnica = models.CharField(max_length=30)
    predmet = models.CharField(max_length=30)
    version = models.CharField(max_length=9)
    swap = models.ForeignKey(Swaps)


class Bidders(models.Model):
    user = models.OneToOneField(User)
    vpisna = models.CharField(max_length=8)
    urnikVersion = models.CharField(max_length=9)

class Parsedoffers(models.Model):
    user = models.ForeignKey(User)
    termin = models.CharField(max_length=30)
    ucilnica = models.CharField(max_length=30)
    predmet = models.CharField(max_length=30)
    offered = models.BooleanField(default=False)
    version = models.CharField(max_length=9)
