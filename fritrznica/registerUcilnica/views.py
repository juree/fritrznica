# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def user_register(username, password, firstname, lastname,vpisna_st):

    user = User.objects.create_user(username,vpisna_st,password)
    user.first_name = firstname
    user.last_name = lastname
    user.save()