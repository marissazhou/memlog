#!/usr/bin/env python
# -*- coding: ascii -*-

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = 'Lijuan Marissa Zhou(marissa.zhou.cn@gmail.com)'
__copyright__ = 'Copyright (c) 2011-2014 Lijuan Marissa Zhou'
__license__ = 'License, see LICENSE for more details'
__vcs_id__ = '$Id$'
__version__ = '0.1' #Versioning: http://www.python.org/dev/peps/pep-0386/

"""
Things to do
Split none views to common folder
"""

import datetime
import json

from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.template import loader, Context
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.template.context import RequestContext
from django.contrib.auth.models import User, Group
from django.utils import simplejson

#from fileuploader 
from utils import *
from memlog_settings import *
from sensor import *
from db.annotaterHelper import * 
from db.eventsegHelper import * 
from models import AnnotationAction

def index(request):
	"""
	"""
	user 		= request.user
	uid         = user.id
	if uid == None:
	#	return render_to_response('lifelog_view/index.html', None, context_instance=RequestContext(request))
		template = loader.get_template('index.html')
		para_view = {}
		context = RequestContext(request, para_view)
		response = template.render(context)
		return HttpResponse(response)
	#print request
	if request.is_ajax():
	#	print "is ajax" 
	#	print "-------------------------"
		message 	= 'annotater index'
		message_suc = 'Successfully added annotations!'

		if 'last_selected_date' in request.REQUEST:
			last_selected_date = request.REQUEST['last_selected_date']
			try:
				cur_album= db_annotater_get_date_album(last_selected_date,uid)
				print cur_album
				print "cur_album ..." 
			except KeyError:
				print "KeyError"
			return HttpResponse(simplejson.dumps({"cur_album":cur_album}), mimetype='application/json')

		elif 'post_mark' in request.REQUEST:
			post_mark	= request.REQUEST['post_mark']
			message 	= 'Please select both image and terms!'
			try:
				if post_mark == "an": #annotation post
					process_request_annotation(request,uid)
				elif post_mark == "ad": #add term 
					process_request_add_term(request,uid)
				elif post_mark == "dd": #delete term
					process_request_delete_term(request,uid)
				elif post_mark == "sa": #select annotatee
					process_request_select_annotatee(request,uid)
			except KeyError:
				print "KeyError"
		return HttpResponse(simplejson.dumps({"message":message_suc}), mimetype='application/json')

    ##########################################
    #### data to be presented ################
    ##########################################
	annotation_terms= db_get_annotation_terms(uid)
	activity_terms  = annotation_terms
	term_categories = annotation_terms.keys() # category of annotation terms
	(album_dates, albums) = db_annotater_get_user_album_data(uid)
	annotatees = db_annotater_get_user_annotatees(uid)

	para_view = {'album_dates'  : json.dumps(album_dates), \
                'anno_terms'    : annotation_terms, \
                'annotatees'  	: annotatees, \
                'albums'        : json.dumps(albums)}
    ##########################################
    #### render              #################
    ##########################################
	return render_to_response('annotater/index.html', para_view, context_instance=RequestContext(request))

def event_annotater(request):
	"""
	This is the index view for annotater, mainly designed by Brain Moynagh
	"""
    ##########################################
    #### data to be presented ################
    ##########################################
	annotation_terms= db_get_annotation_terms(request.user.id)
	activity_terms 	= annotation_terms
	term_categories = annotation_terms.keys() # category of annotation terms
	(album_dates, albums) = db_annotater_get_user_album_data(request.user.id)
	#print "=============================="
	#print (album_dates)
	#print "=============================="
	para_view = {'album_dates'  : json.dumps(album_dates), \
				'anno_terms'    : annotation_terms, \
				'albums'		: json.dumps(albums)}

	# an annotater user
	if user.groups.filter(name=group_name_annotater).exists():
		return render_to_response('annotater/event_annotater.html', para_view, context_instance=RequestContext(request))

def add_term(request):
	"""
	This is the view that receive the added terms from user and insert into database
	"""
	# process requests
	if request.method == 'POST':
		concept = request.REQUEST["add_term_concept"]
		category= request.REQUEST["add_term_category"]
		new_term= AnnotationTerm(concept=concept,category=category,user=User(id=request.user.id),private=True)
		new_term.save()

		return HttpResponseRedirect('/')
	else:
		print 'request.method is not POST'
	data = {}
	data.update(csrf(request))
	return render_to_response('/', data, context_instance=RequestContext(request))

def delete_image(request):
	"""
	This is to accept delete image command from the interface and delete the image from the database but keep in the local machine. 
	This should not not refresh the page
	TODO: 
		1. Should we keep the image in the local machine or not.
		2. Just give image a mark to mark it as deleted or not, but actually not deleted;
		3. Make a statement saying that all images if deleted by user, will be permentatly deleted in the system;
	"""
	# process requests
	if request.method == 'POST':
		image_ids	= request.REQUEST["image_ids"]
		image_ids	= image_ids.split(',')
		for imgId in image_ids:
			db_delete_one_image(int(imgId))
	else:
		print 'request.method is not POST'
	data = {}
	return HttpResponseRedirect('/')

@csrf_exempt
def submit_image_annotation(request):
	"""
	This is to accept image annotations and save into the database 
	This should not not refresh the page
	TODO: 
		1. S
	"""
	user = request.user
	uid  = user.id
	# process requests
	if request.method == 'POST':
		print "------------------------------"
		message 	= 'something wrong!'
		image_ids	= request.REQUEST["image_ids"]
		if image_ids:
			print "insert annotation"
			image_ids		= image_ids.split(',')
			print image_ids
			print "------------------------------"
			annotation_term_ids= request.REQUEST["annotation_terms"]
			print annotation_term_ids
			if annotation_term_ids: 
				annotation_term_ids= annotation_term_ids.split(',')
				print annotation_term_ids
				print "------------------------------"
				db_annotater_insert_user_annotation(uid, image_ids, annotation_term_ids)
			db_annotater_insert_user_annotation_event(uid, image_ids, annotation_terms)
		return HttpResponse(simplejson.dumps({"message":message}), mimetype='application/json')
	data = {}
	return render_to_response('/', data, context_instance=RequestContext(request))

def process_request_annotation(request,uid):
	"""
	This is to accept image annotations and save into the database 
	This should not not refresh the page
	TODO: 
		1. S
	"""
	print "--image_ids----------------------------"
	image_ids	= request.REQUEST.getlist('image_ids[]')
	print image_ids
	if image_ids:
		print "insert annotation"
		print "------------------------------"
		annotation_term_ids= request.REQUEST.getlist("annotation_terms[]")
		print annotation_term_ids
		if annotation_term_ids: 
			print "------------------------------"
			db_annotater_insert_user_annotation(uid, image_ids, annotation_term_ids)

def process_request_add_term(request,uid):
	"""
	"""
	concept = request.REQUEST.get('concept')
	print concept 
	if concept:
		print "------------------------------"
		category = request.REQUEST.get("category")
		if category: 
			print category
			print "------------------------------"
			db_annotater_insert_annotation_term(uid, concept, category)


def process_request_delete_term(request,uid):
	"""
	This is to delete term from the database
	"""
	print "--image_ids----------------------------"

def process_request_select_annotatee(request,uid):
	"""
	This is to switch annotatees for annotators 
	"""
	print "--image_ids----------------------------"
