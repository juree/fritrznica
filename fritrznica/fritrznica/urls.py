from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fritrznica.views.home', name='home'),
    # url(r'^fritrznica/', include('fritrznica.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    (r'^prva/$', 'prva.views.user_login'),
    (r'^$', 'prva.views.redirect_to_login'),
    (r'^registracija/$', 'registracija.views.user_register'),
    (r'^trznica/$', 'trznica.views.trznica_main'),
    (r'^aktivacija/$', 'activateaccount.views.activate_acc'),
    (r'^logout/$', 'prva.views.user_logout'),
)
