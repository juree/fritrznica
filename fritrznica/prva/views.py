# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


def user_login(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #successfully logged in
                return HttpResponseRedirect("/trznica/")
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('prva.html', RequestContext(request,{'state': state, 'username': username}))

def redirect_to_login(request):
    return HttpResponseRedirect("/prva/")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/prva/")