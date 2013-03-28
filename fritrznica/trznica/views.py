# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def trznica_main(request):
    if request.user.has_perm('fritrznica.activated'):
        return render_to_response('trznica.html', RequestContext(request))
    else:
        return render_to_response('activate.html', RequestContext(request))