How to Deploy
=============
This documentation describes how to deploy the lifelog probe system 

Software Requiremnts:
------------
In order to successfully run the prototype code, all following rerequisited packages/softwares are necessary to be installed beforehand.

- Django (1.5.4)
- mod_python
- django-bootstrap-staticfiles (3.0.0.1)
- django-bootstrap-toolkit (2.15.0)
- django-suit (0.2.5)
- ipython (1.1.0)
- matplotlib (1.3.0)
- MySQL-python (1.2.4)
- nose (1.3.0)
- numpy (1.7.1)
- pip (1.4.1)
- pip-tools (0.3.4)
- psycopg2 (2.5.1)
- pyparsing (2.0.1)
- python-dateutil (2.1)
- scipy (0.12.0)
- setuptools (0.9.8)
- six (1.4.1)
- tornado (3.1.1)
- wsgiref (0.1.2)
- easy-thumbnails
- django_php
- Celery(3.1)
- django-admin-tools
- openpyxl
- django-haystack

For Unbuntu 12.04 system, the commands for deployment:

- 
Refer to: https://docs.djangoproject.com/en/dev/topics/install/


.. note:: upgrading from lower version? Checkout :ref:`upgrading`.


To install ``MySQLdb`` module, download it from MySQLdb Download page and proceed as follows `pip`_::
url:http://sourceforge.net/projects/mysql-python/

$ gunzip MySQL-python-1.2.2.tar.gz
$ tar -xvf MySQL-python-1.2.2.tar
$ cd MySQL-python-1.2.2
$ python setup.py build
$ python setup.py install

To install mod_python
---------------------
http://www.djangoproject.com/r/mod_python/
mod_python (http://www.djangoproject.com/r/mod_python/) is an Apache plug-in that embeds Python within Apache and loads Python code into memory when the server starts. Code stays in memory throughout the life of an Apache process, which leads to significant performance gains over other server arrangements.


To install easy-thumbnails
--------------------------
sudo pip install easy-thumbnails

For Mac OS 10.0.9 system, the commands for deployment:
-------------------------------------------------------
you can use the commands like 
pip install MySQL-python 

To install django_php
---------------------
$ pip install django_php
# or
$ easy_install django_php
reference: url:http://animuchan.net/django_php/

PHP Setting
-----------
Install 

   .. code-block:: python 
      :linenos:

	  pip install django_php

In settings.py file
PHP_CGI = '/usr/bin/php-cgi' if server is Ubuntu Linux 
PHP_CGI = '/usr/bin/php-cgi' if server is Mac OS 
For some systems this might be installed, but for ubuntu, it might need to be installed through php5-cgi 


To install Celery
-----------------
Celery(3.1)
is a job server, with Redis as the backend
url:http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html

To install rabbitmq-server
--------------------------
sudo apt-get install rabbitmq-server
rabbitmq-server
url:http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html#first-steps
examples:https://github.com/celery/celery/tree/master/examples

Memcached
---------
By far the fastest, most efficient type of cache available to Django, Memcached is an entirely memory-based cache framework originally developed to handle high loads at LiveJournal.com and subsequently open-sourced by Danga Interactive.
url:https://docs.djangoproject.com/en/dev/topics/cache/#memcached
url:http://memcached.org/

Python-Memcached
----------------
python setup.py install --with-libmemcached=/opt/local

FileUploader
----------------
libs:
- /home/marissa/Documents/software/libs/commons-codec-1.6.jar
- /home/marissa/Documents/software/libs/commons-io-2.4.jar
- /home/marissa/Documents/software/libs/commons-logging-1.1.3.jar
- /home/marissa/Documents/software/libs/fluent-hc-4.3.2.jar
- /home/marissa/Documents/software/libs/httpclient-4.3.2.jar
- /home/marissa/Documents/software/libs/httpclient-cache-4.3.2.jar
- /home/marissa/Documents/software/libs/httpcore-4.3.1.jar
- /home/marissa/Documents/software/libs/httpmime-4.3.2.jar

User Authentication
-------------------
Replace this with file in sys
- /usr/local/lib/python2.7/dist-packages/django/contrib/auth/views.py
- 
start service
-------------
./manage.py runserver 0.0.0.0:9999

django-haystack
---------------
pip install django-haystack

Apache configuration
--------------------
Apache configuration file
- /etc/apache2/httpd.conf
