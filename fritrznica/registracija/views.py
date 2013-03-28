# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

def user_register(request):
    if request.POST:
        userName = request.REQUEST.get('username', None)
        userPass = request.REQUEST.get('password', None)
        userMail = request.REQUEST.get('email', None)

        # TODO: check if already existed

        user = User.objects.create_user(userName, userMail, userPass)
        user.save()

    return render_to_response('registracija.html', RequestContext(request))
