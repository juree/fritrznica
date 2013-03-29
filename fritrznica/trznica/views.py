# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def trznica_main(request):
    ime="Primoz"
    vpisna="63110367"
    priimek="Karnicnik"
    predmet= "IPRI"
    termin1= "PON 7:30- 9:00"
    termin2="PET 7:30-9:00"
    space= " "
    if request.user.is_authenticated():
        if request.user.has_perm('fritrznica.activated'):
            return render_to_response('trznica.html', RequestContext(request,{'termin1': termin1, 'ime': ime, 'priimek': priimek, 'space':space, 'predmet':predmet,'vpisna':vpisna, 'termin2':termin2}))
        else:
            return HttpResponseRedirect("/aktivacija/")
    else:
        return HttpResponseRedirect("/prva/")