from django.conf.urls import patterns, include, url

urlpatterns = patterns('sensecam.views',
    url(r'^$', 'index'),
)
