from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'authUcilnica.views.user_login',
                           name='authURL'),
                       # (r'^authUcilnica/$', 'authUcilnica.views.user_login'),
                       )
