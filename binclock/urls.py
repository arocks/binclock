from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'binclock.views.home', name='home'),
)
