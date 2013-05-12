from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect


def offer(request):
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        return render_to_response('ponudi.html');
