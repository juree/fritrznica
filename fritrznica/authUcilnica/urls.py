from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                        (r'^$', 'authUcilnica.views.redirect_to_login'),
                        (r'^authUcilnica/$', 'authUcilnica.views.user_login'),
)
