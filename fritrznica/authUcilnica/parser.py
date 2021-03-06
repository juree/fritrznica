from bs4 import BeautifulSoup
import urllib2
import re


def parseUrnik(vpisna, version):
    parsed = []
    url = "http://urnik.fri.uni-lj.si/allocations?student=" + vpisna\
          + "&timetable=" + version
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())

    reg = '.*?(allocated).A|LV'
    regex = re.compile(reg, re.IGNORECASE | re.DOTALL)

    vaje = soup.findAll("td", regex)
    for entry in vaje:
        single = entry.find('span').getText().split('\r\n')
        termin = re.sub('\s{2,}',
                        '',
                        single[1]) + " " + re.sub('\s{2,}',
                                                  '',
                                                  single[2])
        ucilnica = re.sub('\s{2,}', '', single[2])
        predmet = re.sub('\s{2,}', '', single[3])
        predmet = re.sub('(\\(.*\\))', '', predmet)
        predmet = predmet.replace("_", " ")
        ent = {"termin": termin, "ucilnica": ucilnica, "predmet": predmet}
        parsed.append(ent)

    return parsed


def parseVersion():
    url = "http://urnik.fri.uni-lj.si"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())

    return '156'
    #return soup.find("input", {"name": "timetable"})["value"]
