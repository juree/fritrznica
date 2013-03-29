# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def trznica_main(request):
    if request.user.is_authenticated():
        if request.user.has_perm('fritrznica.activated'):
            return render_to_response('trznica.html', RequestContext(request))
        else:
            return HttpResponseRedirect("/aktivacija/")
    else:
        return HttpResponseRedirect("/prva/")