from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fritrznica.views.home', name='home'),
    # url(r'^fritrznica/', include('fritrznica.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    (r'^prva/$', 'prva.views.user_login'),
    (r'^$', 'prva.views.redirect_to_login'),
    (r'^registracija/$', 'registracija.views.user_register'),
)
