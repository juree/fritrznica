from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def cakalnica(request):
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        return render_to_response('cakalnica.html',RequestContext(request,{'request': request}));
