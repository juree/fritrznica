from django.db import models
from django.contrib.auth.models import User


class Offers(models.Model):
    user = models.ForeignKey(User)
    termin = models.CharField(max_length=30)
    ucilnica = models.CharField(max_length=30)
    predmet = models.CharField(max_length=30)
    version = models.CharField(max_length=9)
    offered = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    #swap_id=models.IntegerField()


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
    closed = models.BooleanField(default=False)
    #swap_id=models.IntegerField()


class Swaps(models.Model):
    date = models.DateTimeField()
    closed = models.BooleanField(default=False)
    valid = models.BooleanField(default=True)
    offerid = models.IntegerField(default=-1)
    #ponudba z firstfromucilnica
    parsedofferid = models.IntegerField(default=-1)
    #moje vaje


#00 - swaps ni veljaven
#01 - swaps veljaven
#10 - swaps zavrnjen
#11 - swaps sprejet
