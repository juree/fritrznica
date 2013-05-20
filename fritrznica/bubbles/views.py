import csv
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from data.models import Offers


def showBubble(request):
    if not request.user.is_active:
        return HttpResponseRedirect('/authUcilnica/')
    else:
        create_csv()
        return render_to_response('bubbles.html',
                                  RequestContext(
                                      request,
                                      {
                                          'request': request
                                      }
                                  ))


def create_csv():
    predmeti = []
    count = []
    neki = Offers.objects.all()
    for iter in neki:
        string = iter.predmet
        if string not in predmeti:
            predmeti.append(string)
    for iter in predmeti:
        count.append(Offers.objects.filter(predmet=iter).count())
    for i in range(len(predmeti)):
        string = predmeti[i]
        string = string.replace(' in ', ' ')
        string = string.replace(' iz ', ' ')
        string = string.replace(' AV', '')
        string = string.replace(' LV', '')
        string = "".join(e[0] for e in string.split())
        predmeti[i] = string
    with open('static/bubbles/data/data.csv','wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='',
                                quoting=csv.QUOTE_NONE)
        spamwriter.writerow(['name','count'])
        for i in range(len(predmeti)):
            spamwriter.writerow([predmeti[i],count[i]])

    csvfile.close()



