from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

#from fileuploader 
#import views

urlpatterns = patterns('downloader.views',
    url(r'^$', "index", name='index'),
    url(r'researcher^$', "researcher", name='researcher'),
) 

