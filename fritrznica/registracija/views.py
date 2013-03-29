# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def user_register(request):
    username = password = firstname = lastname = state = ''
    if request.POST:
        username = request.REQUEST.get('username', None)
        password = request.REQUEST.get('password', None)
        #email = request.REQUEST.get('email', None)
        firstname = request.REQUEST.get('firstname', None)
        lastname = request.REQUEST.get('lastname', None)

        # TODO: check if already existed

        if username and password and firstname and lastname and not User.objects.filter(username=username).count() > 0:
            user = User.objects.create_user(username, password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
        else:
            state = "Neveljavna registracija"
            return render_to_response('registracija.html', RequestContext(request,{'state': state}))
        return HttpResponseRedirect('/prva/')

    return render_to_response('registracija.html', RequestContext(request))
