import re
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from ucilnica import ucilnica_login
from parser import parseUrnik, parseVersion
from data.models import Parsedoffers


def redirect_to_login(request):
    return HttpResponseRedirect("/authUcilnica/")


def user_logout(request):
    logout(request)
    request.session.flush()
    return HttpResponseRedirect("/authUcilnica/")


def user_login(request):
        state = username = ""
        if request.POST:
            #parse version of timetable first
            urnikVersion = parseVersion()
            vaje = []
            username = request.POST['username']
            password = request.POST['password']
            #check if user already exists
            user = authenticate(username=username, password=password)
            if user is not None:
                #user already in database, don't connect to ucilnica
                #compare timetable versions
                if user.bidders.urnikVersion != urnikVersion:
                    vaje = parseUrnik(user.Bidders.vpisna, urnikVersion)
                    #update database(parsed offers)
                    for ent in vaje:
                        po = Parsedoffers(user=User, termin=ent["termin"], ucilnica=ent["ucilnica"], predmet=ent["predmet"])
                        po.save()
                login(request, user)
                return HttpResponseRedirect("/firstFromUcilnica/")
            #user not in database, connect to ucilnica and get user_info
            user_info = ucilnica_login(username, password)
            if user_info['valid']:
                #user_info from ucilnica is valid, register user and perform login
                #get info first (firstname, lastname, vpisna)
                name = user_info['name']
                name = re.split(" +", name)
                firstname = name[0]
                lastname = name[len(name) - 1]
                vpisna_st = user_info['vpisna_st']
                if vpisna_st is None:
                    #can't test this!
                    state = "Zal se nimas vpisne stevilke."
                    return render_to_response('prijava.html', RequestContext(request, {'state': state, 'username': username}))
                #register user
                user_register(username, password, firstname, lastname, vpisna_st, urnikVersion)
                user = authenticate(username=username, password=password)
                vaje = parseUrnik(user.bidders.vpisna, urnikVersion)
                #update database(parsed offers)
                for ent in vaje:
                    po = Parsedoffers(user=User, termin=ent["termin"], ucilnica=ent["ucilnica"], predmet=ent["predmet"])
                    po.save()
                login(request, user)
                return HttpResponseRedirect("/firstFromUcilnica/")
            else:
                #user_info from ucilnica is invalid! don't do anything
                state = "Preveri svoje uporabniske podatke."
                return render_to_response('prijava.html', RequestContext(request, {'state': state, 'username': username}))
        return render_to_response('prijava.html', RequestContext(request, {'state': state, 'username': username}))
        state = ""


def user_register(username, password, firstname, lastname, vpisna_st, urnik_version):
        user = User.objects.create_user(username, None, password)
        user.first_name = firstname
        user.last_name = lastname
        user.bidders.vpisna = vpisna_st
        user.bidders.urnikVersion = urnik_version
        user.save()


    #TODO check if 500 and 404 works.
def server_error(request, template_name='500.html'):
        return render_to_response(template_name,
                                  context_instance=RequestContext(request)
        )


def not_found(request, template_name='404.html'):
        return render_to_response(template_name,
                                  context_instance=RequestContext(request)
        )