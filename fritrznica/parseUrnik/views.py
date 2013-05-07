from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def show_parsed_data(request):
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        return render_to_response('ponudi.html', RequestContext(request))
