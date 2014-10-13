from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

#import views

urlpatterns = patterns('annotater.views',
    url(r'^$', "index", name='index'),
	url(r'^/event$', "event_annotater", name='event_annotater'),
	url(r'^/add_term$', "add_term", name='add_term'),
	url(r'^/delete_image$', "delete_image", name='delete_image'),
	url(r'^/submit_image_annotation$', "index", name='submit_image_annotation'),
) 

