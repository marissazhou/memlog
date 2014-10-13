from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

#from fileuploader 
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^/scatter$', views.scatter, name='scatter'),
    url(r'^/link$', views.link, name='link'),
    url(r'^/timeline$', views.timeline, name='timeline'),
    url(r'^/acc$', views.acc, name='acc'),
    url(r'^/line$', views.line, name='line'),
) 

