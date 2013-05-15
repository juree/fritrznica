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
        #delete if in swaps
        if Swaps.objects.filter(offerid=id).exists():
            swaps=Swaps.objects.filter(offerid=id)
            for entry in swaps:
                entry.valid=False
                entry.save()
        o.offered = False
        o.save()
        po = Parsedoffers.objects.get(id=id)
        po.offered = False
        po.save()
        return HttpResponseRedirect('/firstFromUcilnica/')

def predlagaj_zamenjavo(request, id):
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        o=Offers.objects.get(id=id)
        po=Parsedoffers.objects.get(user_id=request.user.id, predmet=o.predmet, closed=False)
        if po is not None:
            if not Swaps.objects.filter(offerid_id=id, parsedofferid_id=po.id).exists():
                s=Swaps(date=datetime.datetime.now(), closed=False, valid=True, offerid_id=id, parsedofferid_id=po.id)
                s.save()
                return HttpResponseRedirect('/firstFromUcilnica/')
            else:
                #TODO menjava ze obstaja
                return HttpResponseRedirect('/firstFromUcilnica/')
        else:
            #TODO menjava ni mozna
            return HttpResponseRedirect('/firstFromUcilnica/')

