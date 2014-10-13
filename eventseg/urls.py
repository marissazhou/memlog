from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^/event$', views.event, name='event'),
) 

