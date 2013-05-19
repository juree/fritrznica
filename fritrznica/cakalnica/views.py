from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from data.models import Parsedoffers, Offers, Swaps, Bidders
from django.db.models import Q


def cakalnica(request):
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        return render_to_response('cakalnica.html',
                                  RequestContext(
                                      request,
                                      {
                                          'request': request
                                      }
                                  ))


def contribute(request):  # its sux, but works :)
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        version = Bidders.objects.get(user_id=request.user.id).urnikVersion
        userid = request.user.id
        q = Parsedoffers.objects.filter(user_id=userid,
                                        offered=True,
                                        closed=False,
                                        version=version)
                                        # dobim termine ki jih je user ponudu
        predmet = ""
        id = 0
        mojtermin = ""
        list = []
        listzamenjav = []
        for i in range(len(q)):
            listzamenjav = []
            # ent = [q[i].predmet,q[i].termin,q[i].id]
            zamenjave = Swaps.objects.filter(offerid=q[i].id,
                                             closed=False,
                                             valid=True)
            for j in range(len(zamenjave)):
                pid = zamenjave[j].parsedofferid
                zamenjava = Parsedoffers.objects.get(id=pid)
                id_swap = zamenjave[j].id
                toappend = [id_swap,zamenjava.termin]
                listzamenjav.append(toappend)
                # TODO close swap if accepted
            offer = Parsedoffers.objects.get(id=q[i].id)
            predmet = offer.predmet
            mojtermin = offer.termin
            id = q[i].id
            list.append([predmet,id,mojtermin,listzamenjav])
            # list je v formatu [TIS,id,9.00,[tork,petk,pondelk,..]]

        #end
        #-----
        #drugi del

        predmet = ""
        mojtermin = ""
        tujtermin = ""
        id = ""
        mojipredmeti = Parsedoffers.objects.filter(user_id=request.user.id,
                                                   closed=False,
                                                   version=version)
        ustrezne_zamenjave = []
        writeoutlist = []
        for offr in mojipredmeti:
            obj = Swaps.objects.filter(parsedofferid=offr.id,
                                       closed=False,
                                       valid=True)
            for i in range(len(obj)):
                ustrezne_zamenjave.append(obj[i])
        for iter in ustrezne_zamenjave:
            predmet = Parsedoffers.objects.get(id=iter.parsedofferid).predmet
            mojtermin = Parsedoffers.objects.get(id=iter.parsedofferid).termin
            tujtermin = Offers.objects.get(id=iter.offerid).termin
            writeoutlist.append([predmet, mojtermin, tujtermin])

        # end
        # tretji del

        zaprte = Parsedoffers.objects.filter(user_id=request.user.id,
                                             version=version,
                                             closed=True)
        allout = []
        notallout = []
        for iter in zaprte:
            listek = []
            swapek = Swaps.objects.filter(
                Q(offerid=iter.id) | Q(parsedofferid=iter.id),
                closed = True, valid = True)  # magic
            notswapek = Swaps.objects.filter(
                Q(offerid=iter.id) | Q(parsedofferid=iter.id),
                closed=True, valid=False)
            oid = 0
            if len(swapek) != 0:
                oid = swapek[0].parsedofferid
                drug_termin = Parsedoffers.objects.get(id=oid)
                listek = [iter.predmet,iter.termin, drug_termin.termin]
                allout.append(listek)
            if len(notswapek) != 0:
                oid = notswapek[0].parsedofferid
                drug_termin = Parsedoffers.objects.get(id=oid)
                listek = [iter.predmet,iter.termin,drug_termin.termin]
                notallout.append(listek)
        #end

        return render_to_response('cakalnicaSandbox.html',
                                  RequestContext(
                                      request,
                                      {
                                          'request': request,
                                          'termini': list,
                                          'sodelujem': writeoutlist,
                                          'sprejeto': allout,
                                          'zavrnjeno': notallout
                                      }
                                  ))


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
            auto_reject_swaps(swaps, -1)
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
    parsedoffer1 = Parsedoffers.objects.get(id=swap.offerid)
    offer1 = Offers.objects.filter(id=swap.parsedofferid)
    if len(offer1) != 0:
        offer1x = offer1[0]
        offer1x.closed = True
        offer1x.save()

    swap.closed = True
    offer.closed = True
    parsedoffer.closed = True
    parsedoffer1.closed = True
    swap.save()
    offer.save()
    parsedoffer.save()
    parsedoffer1.save()
    #auto reject other swaps
    swaps = Swaps.objects.filter(parsedofferid=swap.parsedofferid,
                                 closed=False)
    auto_reject_swaps(swaps, id)
    swaps = Swaps.objects.filter(offerid=swap.offerid,
                                 closed=False)
    auto_reject_swaps(swaps, id)
    return HttpResponseRedirect('/cakalnica/')

def auto_reject_swaps(swaps, exclid):
    if len(swaps) > 0:
        for entry in swaps:
            if entry.id != exclid:
                entry.closed = True
                entry.valid = False
                entry.save()
