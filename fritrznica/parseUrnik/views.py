from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from UrnikParser import parseUrnik

def zamenjaj_vaje(request):
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        vpisna = request.user.email
        version = "156";
        vaje = parseUrnik(vpisna,version)
        burek = {2,3,6,1}
        return render_to_response('zamenjaj.html', RequestContext(request, {'vpisna': vpisna, 'vaje': vaje, 'burek': burek}))


def show_parsed_data(request):
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        return render_to_response('ponudi.html', RequestContext(request))
