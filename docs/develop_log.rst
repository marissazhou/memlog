Development Logs with Encountered Problems and Solutions
========================================================

Database Error: Lock wait timeout exceeded in MYSQL
---------------------------------------------------
url:http://stackoverflow.com/questions/5836623/getting-lock-wait-timeout-exceeded-try-restarting-transaction-even-though-im

Problem:
~~~~~~~~
ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
 

Cause:
~~~~~~
You are using a transaction; autocommit does not disable transactions, it just makes them automatically commit at the end of the statement. What is happening is, some other thread is holding a record lock on some record for too long, and your thread is being timed out. (by MarkR)
 
You are using a transaction; autocommit does not disable transactions, it just makes them automatically commit at the end of the statement.

What is happening is, some other thread is holding a record lock on some record (you're updating every record in the table!) for too long, and your thread is being timed out.

You can see more details of the event by issuing a "SHOW ENGINE INNODB STATUS" after the event. Ideally do this on a quiet test-machine.


Solution:
~~~~~~~~~
show variables like 'innodb_lock_wait_timeout';
Run SHOW ENGINE INNODB STATUS to see more information.

The default lock wait timeout is 50sec. You can set it by the default innodb_lock_wait_timeout=50 or set it to higher value and restart mysql.

CSRF verification failed. Request aborted.
------------------------------------------
url:https://docs.djangoproject.com/en/dev/ref/contrib/csrf/#ref-contrib-csrf

In any template that uses a POST form, use the csrf_token tag inside the <form> element if the form is for an internal URL, e.g.::
	<form action="." method="post">{% csrf_token %}


Django user.is_authenticated works some places, not others
----------------------------------------------------------

url:http://stackoverflow.com/questions/3337419/django-user-is-authenticated-works-some-places-not-others


name 'login_required' is not defined
------------------------------------

url:http://stackoverflow.com/questions/2164069/best-way-to-make-djangos-login-required-the-default

Solution:
~~~~~~~~~
add this into views.py:: 
	from django.contrib.auth.decorators import login_required

Check bootstrap and jQuery Conflict
-----------------------------------
url:http://jsfiddle.net/QchpT/54/

DropZone
--------
url:http://amatellanes.wordpress.com/2013/11/05/dropzonejs-django-how-to-build-a-file-upload-form/

Can't install PIL after Mac OS X 10.9
-------------------------------------
url:http://stackoverflow.com/questions/19532125/cant-install-pil-after-mac-os-x-10-9


Import modules into an external class
-------------------------------------
django.core.exceptions.ImproperlyConfigured: Requested setting DATABASES, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.

Solution:
~~~~~~~~~
url:http://stackoverflow.com/questions/15556499/django-db-settings-improperly-configured-error
You can't just fire up python and check things, django doesn't know what project you want to work on. You have to do one of these things:

-    Use python manage.py shell
-    Use django-admin.py shell --settings=mysite.settings (or whatever settings module you use)
-    Set DJANGO_SETTINGS_MODULE environment variable in your OS to mysite.settings

-    Use setup_environ in the python interpreter:

    from django.core.management import setup_environ

    from mysite import settings

    setup_environ(settings)

Naturally, the first way is the easiest.

Modify Login View Form
----------------------

