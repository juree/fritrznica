# coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from data.models import Parsedoffers


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
            return HttpResponseRedirect('/offer/')


def offerSwap(request, id):
    #num je ID od data_parsedoffers
    #kle naprej delaš tisto zamenjavo...v num dobiš ID, znjim delaj kar želiš :) Srečno kekec :D
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        return render_to_response('ponudi.html', RequestContext(request, {'request': request}))
        #return render_to_response('ponudi.html', RequestContext(request, {'id':id}))
