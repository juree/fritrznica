# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from data.models import Parsedoffers, Offers, Swaps
import datetime
from django.core.urlresolvers import reverse

def profil(request):
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        return render_to_response('profile.html',RequestContext(request,{'user': request.user}));

def firstFrom_main(request):
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        state = 0
        err = request.GET.get('error', '0')
        succ = request.GET.get('succes', '0')
        if err == "1":
            state = 1 #Nimas ustreznega predmeta za menjavo
        elif err == "2":
            state = 2 #Ponudba ze obstaja
        if succ == "1":
            state = 3 #Uspesno ste ponudili zamenjavo
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
        try:
            po=Parsedoffers.objects.get(user_id=request.user.id, predmet=o.predmet, closed=False)
        except:
            return HttpResponseRedirect('/firstFromUcilnica/?error=1')
        if po is not None:
            if not Swaps.objects.filter(offerid=id, parsedofferid=po.id).exists():
                s=Swaps(date=datetime.datetime.now(), closed=False, valid=True, offerid=id, parsedofferid=po.id)
                s.save()
                return HttpResponseRedirect('/firstFromUcilnica/?succes=1')
            else:
                if Swaps.objects.filter(offerid=id, parsedofferid=po.id, valid=False).exists():
                    s=Swaps.objects.get(offerid=id, parsedofferid=po.id, valid=False)
                    s.valid=True
                    s.save()
                    return HttpResponseRedirect('/firstFromUcilnica/?succes=1')
                else:
                    return HttpResponseRedirect('/firstFromUcilnica/?error=2')