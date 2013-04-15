##TODO: pass a username,vpisna_st,firstname...to firstpage

from ucilnica import ucilnica_login
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from registerUcilnica.views import user_register
from firstFromUcilnica.views import firstFrom_main
from django.core.urlresolvers import reverse
import re

def redirect_to_login(request):
    return HttpResponseRedirect("/authUcilnica/")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/authUcilnica/")


def user_login(request):
    state = "Please log in below..."
    username=password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request,user)
                return HttpResponseRedirect("/firstFromUcilnica/")
        user_info = ucilnica_login(username,password)
        if user_info['valid']:
            name = user_info['name']
            id = user_info['ucilnica_id']
            vpisna_st = user_info['vpisna_st']
            if user is not None:
                login(request, user)
                #successfully logged in
                return HttpResponseRedirect("/firstFromUcilnica/")
            else:
                name = re.split(" +",name)
                firstname = name[0]
                lastname = name[len(name)-1]
                user_register(username,password,firstname,lastname,vpisna_st)
                user = authenticate(username=username, password=password)
                login(request,user)
                return HttpResponseRedirect("/firstFromUcilnica/")
                #state = "Your username and/or password were incorrect."
                #state = "Login error"
                #return HttpResponseRedirect("/firstFromUcilnica/")
    return render_to_response('authUcilnica.html', RequestContext(request,{'state': state, 'username': username}))
    state = ""