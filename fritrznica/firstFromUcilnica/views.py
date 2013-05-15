# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from data.models import Parsedoffers, Offers, Swaps
import datetime


def profil(request):
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        return render_to_response('profile.html',RequestContext(request,{'user': request.user}));

def firstFrom_main(request):
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        username = request.user
        vpisna = username.email
        ime = username.first_name
        priimek = username.last_name
        return render_to_response('firstFromUcilnica.html',RequestContext(request,{'username': username, 'vpisna': vpisna, 'ime': ime, 'priimek': priimek, 'request': request}))

def brisi_ponudbo(request, id):
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        #funkcija bo vezana na drug url (/brisi) in id bo vedno podan
        o = Offers.objects.get(id=id)
        if o.swap_id > 0:
            s = Swaps.objects.get(id=o.swap_id)
            s.valid = False
        o.offered = False
        o.save()
        po = Parsedoffers.objects.get(id=id)
        po.offered = False
        po.save()
        return HttpResponseRedirect('/firstFromUcilnica/')

def predlagaj_zamenjavo(request, myid, yourid):
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        s=Swaps(date=datetime.datetime.now(), closed=False, valid=True, offerid=yourid, parsedofferid=myid)
        s.save()
        return HttpResponseRedirect('/firstFromUcilnica/')


