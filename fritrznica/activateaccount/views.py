# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def activate_acc(request):
    #activation failed
    return render_to_response('activate.html', RequestContext(request))
    #activation complete
    #return HttpResponseRedirect("/trznica/")