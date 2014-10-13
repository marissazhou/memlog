#!/usr/bin/env python
# -*- coding: ascii -*-

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ 		= 'Lijuan Marissa Zhou(marissa.zhou.cn@gmail.com)'
__copyright__ 	= 'Copyright (c) 2011-2014 Lijuan Marissa Zhou'
__license__ 	= 'License, see LICENSE for more details'
__vcs_id__ 		= '$Id$'
__version__ 	= '0.1' #Versioning: http://www.python.org/dev/peps/pep-0386/

"""
Things to do
Split none views to common folder
"""

import os
import sys


new_path_common = sys.path[0]+'/lib/common'
if new_path_common not in sys.path:
        sys.path.append(new_path_common)
new_path_lib = sys.path[0]+'/lib'
if new_path_lib not in sys.path:
        sys.path.append(new_path_lib)
new_path_logic = sys.path[0]+'/lib/logic'
if new_path_logic not in sys.path:
        sys.path.append(new_path_logic)
#sys.path.append(sys.path[0]+'/lib')
#sys.path.append(sys.path[0]+'/lib/logic')
#sys.path.append(sys.path[0]+'/lib/common')

import datetime
import json
from django.utils import simplejson
from django.utils.decorators import * 

from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_response_exempt

from django.http import HttpResponse
from django.views.generic.base import View
from django.template import loader, Context
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template.context import RequestContext
from django.contrib.sites.models import Site
from django.contrib.auth.models import User, Group

from utils import *
from settings import *
from sensor import *
from db.annotaterHelper import *
from db.healthHelper import *
from db.authHelper import *

uid = 3
username = "anonymous"

def index(request):
	""" This function processes all unuploaded sensecam files directly from sensecam devices, these sensecam files are not previously uploaded using sensecam software.

	:param  capture_time: capture time of this file, only available for image files 
	:type   capture_time: datetime.datetime 

	:return: None
	"""
	global uid
	global username
	#print "-------sensecam_browser index------"
	#print uid 
	#print username 
	#print "----------------------------------"

	if request.user.is_authenticated():
		user 		= request.user
		username    = user.username
		uid         = user.id
		return my_lifelog(request)
	else:
		template = loader.get_template('index.html')
		para_view = {}
		context = RequestContext(request, para_view)
		response = template.render(context)
		return HttpResponse(response)

def index_gallery(request):
	""" This function processes all unuploaded sensecam files directly from sensecam devices, these sensecam files are not previously uploaded using sensecam software.

	:param  capture_time: capture time of this file, only available for image files 
	:type   capture_time: datetime.datetime 
	:return: None
	"""
	template = loader.get_template('index_gallery.html')
	para_view = {}
	context = Context(para_view)
	response = template.render(context)
	return HttpResponse(response)

#@csrf_response_exempt
#@csrf_exempt
#@ensure_csrf_cookie
def my_lifelog(request):
	""" This is the index view for annotater, mainly designed by Brain Moynagh

	:param  request: 
	:type   request: 
	:return: None
	"""
	##########################################
	#### data to be presented ################
	##########################################
	global uid
	global username
	
	#print "---------------------"
	#print request
	#print uid
	#print username
	#print "in my_lifelog"
	#print "---------------------"
	if request.is_ajax():
		message     = "is ajax in my_lifelog"
		cur_album	= None
		# print "is ajax in my_lifelog"
		if 'last_selected_date' in request.REQUEST:
			last_selected_date = request.REQUEST['last_selected_date']
			try:
				cur_album= db_annotater_get_date_album(last_selected_date,uid)
			except KeyError:
				print "KeyError"
		return HttpResponse(simplejson.dumps({"cur_album":cur_album}), mimetype='application/json')
		#return render_to_response('lifelog_view/index.html', para_view, context_instance=RequestContext(request))

	# request is not ajax
	annotation_terms= db_get_annotation_terms(uid)
	activity_terms 	= annotation_terms
	term_categories = annotation_terms.keys() # category of annotation terms
	(album_dates, albums) 	= db_annotater_get_user_album_data(uid)
	#print (album_dates, albums)
	#print album_dates
	#print len(albums)
	activities 				= db_get_all_daily_activities(uid)
	print "=============================="
	"""
	print album_dates
	print annotation_terms
	print albums
	"""
	para_view = {'album_dates'  : json.dumps(album_dates), \
				'anno_terms'    : annotation_terms, \
				'albums'		: json.dumps(albums), \
				'activities'	: json.dumps(activities)}
	##########################################
	#### render              #################
	##########################################
	return render_to_response('lifelog_view/index.html', para_view, context_instance=RequestContext(request))

def assign_task(request):
	""" This function This is for administrater to assign tasks to annotaters
	:param  request: 
	:type   request: 
	:return: None
	"""
	annotation_tasks= {"user1":["user2"]}
	annotators 		= db_auth_all_group_users_annotation("annotator")
	subjects		= db_auth_all_group_users_annotation("subject")

	if request.method == 'POST':
		return HttpResponse(simplejson.dumps(annotation_tasks), mimetype='application/json')

	# initial view
	para_view = {'annotation_tasks': annotation_tasks, \
				'subjects'      : subjects, \
				'annotators'	: annotators}
	return render_to_response('annotater/task_assignment.html', para_view, context_instance=RequestContext(request))

def public_about(request):
	""" This fu
	:param  request: 
	:type   request: 
	:return: None
	"""
	# initial view
	para_view = {}
	return render_to_response('public/about.html', para_view, context_instance=RequestContext(request))

def public_publications(request):
	""" This fu
	:param  request: 
	:type   request: 
	:return: None
	"""
	# initial view
	para_view = {}
	return render_to_response('public/publications.html', para_view, context_instance=RequestContext(request))

