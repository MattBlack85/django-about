from django.conf.urls import patterns, url

from .views import about


urlpatterns = patterns('',
                       url(r'^$', about, name='about'),
                       )
