from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

#from fileuploader 
#import views

urlpatterns = patterns('fileuploader.views',
    url(r'^$', "index", name='index'),
) 

