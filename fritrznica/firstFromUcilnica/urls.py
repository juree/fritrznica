from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       (r'^$', 'firstFromUcilnica.views.firstFrom_main'),
                       (r'^$/(?P<error>\d+)/$', 'firstFromUcilnica.views.firstFrom_main'),
                       (r'^$/(?P<succes>\d+)/$', 'firstFromUcilnica.views.firstFrom_main'),
                       #(r'^$', 'firstFromUcilnica.views.firstFrom_mainn'),

)