# coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect


def offer(request):
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        return render_to_response('ponudi.html')

def offerSwap(request,num):
    #num je ID od data_parsedoffers
    #kle naprej delaš tisto zamenjavo...v num dobiš ID, znjim delaj kar želiš :) Srečno kekec :D
    return 0 #da ni errorjev trenutno