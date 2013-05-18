from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from data.models import Parsedoffers, Offers, Swaps


def cakalnica(request):
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        return render_to_response('cakalnica.html',RequestContext(request,{'request': request}))

def contribute(request): #its sux, but works :)
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        userid=request.user.id
        q = Parsedoffers.objects.filter(user_id=userid, offered = True) #dobim termine ki jih je user ponudu
        predmet=""
        id=0
        mojtermin=""
        list = []
        listzamenjav=[]
        for i in range(len(q)):
            listzamenjav = []
            #ent = [q[i].predmet,q[i].termin,q[i].id]
            zamenjave=Swaps.objects.filter(offerid=q[i].id)
            for j in range(len(zamenjave)):
                pid = zamenjave[j].parsedofferid
                zamenjava = Parsedoffers.objects.get(id=pid)
                listzamenjav.append(zamenjava.termin)
                #TODO close swap if accepted
            offer = Parsedoffers.objects.get(id=q[i].id)
            predmet = offer.predmet
            mojtermin = offer.termin
            id=q[i].id
            list.append([predmet,mojtermin,id,listzamenjav]) #list je v formatu [TIS,9.00,1,[tork,petk,pondelk,..]]

        #end
        #-----
        #drugi del
        predmet = ""
        mojtermin=""
        tujtermin=""
        id =""
        mojipredmeti = Parsedoffers.objects.filter(user_id=request.user.id)
        ustrezne_zamenjave = []
        writeoutlist = []
        for offr in mojipredmeti:
            obj = Swaps.objects.filter(parsedofferid=offr.id)
            for i in range(len(obj)):
                ustrezne_zamenjave.append(obj[i])
        for iter in ustrezne_zamenjave:
            predmet = Parsedoffers.objects.get(id=iter.parsedofferid).predmet
            mojtermin = Parsedoffers.objects.get(id=iter.parsedofferid).termin
            tujtermin = Offers.objects.get(id=iter.offerid).termin
            writeoutlist.append([predmet,mojtermin,tujtermin])
        #end
        return render_to_response('cakalnicaSandbox.html',RequestContext(request,{'request': request,'termini': list, 'sodelujem': writeoutlist}))
        return 0

def brisi_ponudbo(request, id):
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        #funkcija bo vezana na drug url (/brisi) in id bo vedno podan
        o = Offers.objects.get(id=id)
        if o.user_id == request.user.id:
            po = Parsedoffers.objects.get(id=id)
            #delete if in swaps
            swaps=Swaps.objects.filter(parsedofferid = id)
            auto_reject_swaps(swaps)
            o.offered = False
            o.save()
            po.offered = False
            po.save()
            return HttpResponseRedirect('/cakalnica/')

def sprejmi_zamenjavo(request, id):
    #handle both offers
    swap = Swaps.objects.get(id=id)
    offer = Offers.objects.get(id=swap.offerid)
    parsedoffer = Parsedoffers.objects.get(id=swap.parsedofferid)
    swap.closed = True
    offer.closed = True
    parsedoffer.closed = True
    swap.save()
    offer.save()
    parsedoffer.save()
    #auto reject other swaps
    swaps = Swaps.objects.filter(parsedofferid=swap.parsedofferid)
    auto_reject_swaps(swaps)
    swaps = Swaps.objects.filter(offerid=swap.offerid)
    auto_reject_swaps(swaps)
    return HttpResponseRedirect('/cakalnica/')

def auto_reject_swaps(swaps):
    if len(swaps) > 0:
        for entry in swaps:
            entry.closed=True
            entry.valid=False
            entry.save()