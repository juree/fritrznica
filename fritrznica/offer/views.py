# coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from data.models import Parsedoffers, Offers


def offer(request, id=-1):
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        if id < 0:
            #ID ni podan
            return render_to_response('ponudi.html', RequestContext(request, {'request': request}))
        else:
            #ID = offer.id
            off=Parsedoffers.objects.get(id=id)
            off.offered = True
            off.save()
            if Offers.objects.filter(id=id).exists():
                off1=Offers.objects.get(id=id)
                off1.offered=True
                off1.save()
            else:
                off1=Offers(id=id, user_id=off.user_id, termin=off.termin, ucilnica=off.ucilnica, predmet=off.predmet, version=off.version, swap_id=-1, offered=True, closed=False)
                off1.save()
            return HttpResponseRedirect('/offer/')


def offerSwap(request, id):
    #num je ID od data_parsedoffers
    #kle naprej delaš tisto zamenjavo...v num dobiš ID, znjim delaj kar želiš :) Srečno kekec :D
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        return render_to_response('ponudi.html', RequestContext(request, {'request': request}))
        #return render_to_response('ponudi.html', RequestContext(request, {'id':id}))
