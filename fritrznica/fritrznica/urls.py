#from django.conf.urls import patterns, include, url
from django.contrib import admin
from firstFromUcilnica.resources import OffersResource
from offer.resources import ParsedoffersResource
from tastypie.api import Api
from django.conf.urls import *

admin.autodiscover()
offers_resource = OffersResource()
v1_api = Api(api_name='v1')
v1_api.register(OffersResource())
v1_api.register(ParsedoffersResource())

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'fritrznica.views.home', name='home'),
                       # url(r'^fritrznica/', include('fritrznica.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       url(r'^admin/', include(admin.site.urls)),

                       # (r'^prva/$', 'prva.views.user_login'),
                       (r'^$', include('authUcilnica.urls')),
                       #(r'^authUcilnica/$', 'authUcilnica.views.user_login',),
                       (r'^authUcilnica/$', include('authUcilnica.urls')),
                       (r'^logout', 'django.contrib.auth.views.logout',
                        {'next_page': '/authUcilnica/'}),
                       (r'^firstFromUcilnica/$', include('firstFromUcilnica.urls')),
                       (r'^profil/$','firstFromUcilnica.views.profil'),
                       (r'^offer/$','offer.views.offer'),
                       (r'^offer/(?P<id>\d+)/$','offer.views.offerSwap'),
                       (r'^api/',include(v1_api.urls)),

                       # (r'^registracija/$', 'registracija.views.user_register'),
                       # (r'^trznica/$', 'trznica.views.trznica_main'),
                       # (r'^aktivacija/$', 'activateaccount.views.activate_acc'),
                       #(r'^logout/$', 'prva.views.user_logout'),
                       #TODO handle user without vpisna_st
)
