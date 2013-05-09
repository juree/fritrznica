from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       (r'^$', 'firstFromUcilnica.views.firstFrom_main'),
                       #(r'^$', 'firstFromUcilnica.views.firstFrom_mainn'),

)