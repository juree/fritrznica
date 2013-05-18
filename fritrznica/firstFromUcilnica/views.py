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
        state=""
        username = request.user
        vpisna = username.email
        ime = username.first_name
        priimek = username.last_name
        return render_to_response('firstFromUcilnica.html',RequestContext(request,{'username': username, 'vpisna': vpisna, 'ime': ime, 'priimek': priimek, 'request': request, 'state': state}))

def predlagaj_zamenjavo(request, id):
    state = ""
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        o=Offers.objects.get(id=id)
        po=Parsedoffers.objects.get(user_id=request.user.id, predmet=o.predmet, closed=False)
        if po is not None:
            if not Swaps.objects.filter(offerid=id, parsedofferid=po.id).exists():
                s=Swaps(date=datetime.datetime.now(), closed=False, valid=True, offerid=id, parsedofferid=po.id)
                s.save()
                return HttpResponseRedirect('/firstFromUcilnica/')
            else:
                if Swaps.objects.filter(offerid=id, parsedofferid=po.id, valid=False).exists():
                    s=Swaps.objects.get(offerid=id, parsedofferid=po.id, valid=False)
                    s.valid=True
                    s.save()
                    return HttpResponseRedirect('/firstFromUcilnica/')
                else:
                    state="Menjava ze obstaja!"
                    username = request.user
                    vpisna = username.email
                    ime = username.first_name
                    priimek = username.last_name
                    return render_to_response('firstFromUcilnica.html',RequestContext(request,{'username': username, 'vpisna': vpisna, 'ime': ime, 'priimek': priimek, 'request': request, 'state': state}))
        else:
            state="Menjava ni mozna!"
            username = request.user
            vpisna = username.email
            ime = username.first_name
            priimek = username.last_name
            return render_to_response('firstFromUcilnica.html',RequestContext(request,{'username': username, 'vpisna': vpisna, 'ime': ime, 'priimek': priimek, 'request': request, 'state': state}))

