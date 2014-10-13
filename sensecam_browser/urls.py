from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from sensecam_browser import views
from auth.forms import CoheAuthenticationForm


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^assign_task$', views.assign_task, name='assign_task'),
    url(r'^gallery$', views.index_gallery, name='index_gallery'),
    url(r'^sensecam', include('sensecam.urls')),
    url(r'^fileuploader', include('fileuploader.urls')),
    url(r'^downloader', include('downloader.urls')),
    url(r'^annotater', include('annotater.urls')),
    url(r'^eventseg', include('eventseg.urls')),
    url(r'^visualization', include('visualization.urls')),
    # url(r'^search/', include('haystack.urls')),
	(r'^search', include('haystack.urls')),
    url(r'^lifelogview$', views.my_lifelog, name='lifelogview'),
    url(r'^about$', views.public_about, name='public_about'),
    url(r'^publications$', views.public_publications, name='public_publications'),
    # url(r'^', {'template_name': 'lifelog_view/index.html'}),
    # Examples:
    # url(r'^$', 'sensecam_browser.views.home', name='home'),
    # url(r'^sensecam_browser/', include('sensecam_browser.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # application in this website service
    url(r'^contact', include('contact.urls')),
    url(r'^accounts/login/?$','django.contrib.auth.views.login',{'template_name': 'registration/login.html', \
'authentication_form': CoheAuthenticationForm}), (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
	# url(r'^accounts/logout/$','django.contrib.auth.views.logout',{'template_name': '/'),

    # url for registration
    # (r'^accounts/', include('registration.urls')), # this is deprecated
    (r'^accounts/', include('registration.backends.default.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#With this you can serve the static media from Django when DEBUG=True (when you are on local computer) but you can let your web server configuration serve static media when you go to production and DEBUG=False
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)

