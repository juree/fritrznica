# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


def firstFrom_main(request):

    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        username = request.user
        vpisna = username.email
        ime = username.first_name
        priimek = username.last_name
        return render_to_response('firstFromUcilnica.html',RequestContext(request,{'username': username, 'vpisna': vpisna, 'ime': ime, 'priimek': priimek}))

