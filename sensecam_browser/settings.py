from __future__ import absolute_import
# ^^^ The above is required if you want to import from the celery
# library.  If you don't have this then `from celery.schedules import`
# becomes `proj.celery.schedules` in Python 2.x since it allows
# for relative imports by default.

# Celery settings

BROKER_URL = 'amqp://guest:guest@localhost//'

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND='djcelery.backends.cache:CacheBackend'
CELERY_TASK_RESULT_EXPIRES=3600

# Django setting for sensecam_browser project
import os
import sys
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
#TEMPLATE_DEBUG = False#DEBUG

ADMINS = (
    ('Marissa Zhou', 'marissa.zhou.cn@gmail.com'),
)

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'sensecambrowser',
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    # 'MENU': (
    #     'sites',
    #     {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
    #     {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    # ),

    # misc
    # 'LIST_PER_PAGE': 15
}


MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sensecambrowser', # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        # 'USER': 'sensecamuser',
        # 'PASSWORD': 'sensecambrowserpass',
        'USER': 'root',
        'PASSWORD': 'sensepass',
        'HOST': '', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Dublin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/home/media/sensecambrowser/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
# MEDIA_URL = '/media/'
MEDIA_URL = '/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
#STATIC_ROOT = '/var/www/sensecam_browser/static/'
STATIC_ROOT = os.path.join(sys.path[0],'static/')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'krkol^jvc(uhifvoax8@rdat9p-4z_aa84weym%@5mtebbar)a'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
	# for caching
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sensecam_browser.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'sensecam_browser.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.contrib.messages.context_processors.messages',
	'django.contrib.auth.context_processors.auth',
	# this is for suit
    'django.core.context_processors.request',
	# this is self defined processor for global variables in all templates
	'annotater.context_processors.is_annotator_processor',
	# 'sensecam_browser.context_processors.authentication_processor',
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps installed for this project
    # For admin skin (http://django-suit.readthedocs.org/en/develop/)
    # Free to use for non-commercial projects

	# Added.
    'suit',
    'bootstrap_toolkit',
    'django_bootstrap_staticfiles',
    # 'django_php',
	'djcelery',
    'haystack',


    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',


    # apps in this project
    # refer to http://devdoodles.wordpress.com/2009/02/16/user-authentication-with-django-registration/
    'registration',
    'easy_thumbnails',
    'sensecam',
    'fileuploader',
    'eventseg',
    'visualization',
    'annotater',
    'downloader',
    'logger',
    'health',
)

# Python has a debugging mail server available for this purpose.
# Just execute this command and you'll have a mailserver running at port 1025
# python -m smtpd -n -c DebuggingServer localhost:1025

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
EMAIL_HOST              = '136.206.46.144'
EMAIL_PORT				= 1025
EMAIL_HOST_USER			= ''
EMAIL_HOST_PASSWORD		= ''
EMAIL_USE_TLS 			= False
DEFAULT_FROM_EMAIL      = 'webmaster@memorizelife.com'
LOGIN_REDIRECT_URL      = '/'
EMAIL_SUBJECT_PREFIX	= '[Django LifelogBrowser] '
SEND_BROKEN_LINK_EMAILS = True

MANAGERS = (
    ('Marissa Zhou', 'marissa.zhou.cn@gmail.com'),
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#Defining the user profile model
AUTH_PROFILE_MODULE = "UserProfile"

THUMBNAIL_ALIASES = {
    '': {
	'avatar': {'size': (50, 50), 'crop': True},
	'thumb_event': {'size': (100, 100), 'crop': True},
    },
}

#PHP_CGI = '/usr/bin/php-cgi'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '0.0.0.0:9999',
    }
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr',
        # 'URL': 'http://136.206.46.144:8983/solr',
        #'URL': 'http://0.0.0.0:9969/solr'
        # ...or for multicore...
        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    },
}
