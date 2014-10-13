"""dabatabase manipulation class
.. module:: annotaterHelper
   :platform: Ubuntu Unix
   :synopsis: A module for conducting all database annotater.

.. moduleauthor:: Lijuan Marissa Zhou <marissa.zhou.cn@gmail.com>
.. copyright:: copyright reserved 

"""
import unicodedata
from datetime import datetime

from utils import *
from timeutils import *
from time import gmtime, strftime

from django.core.exceptions import ValidationError

from annotater.models import *
from fileuploader.models import *
from django.db.models import Q 
from eventsegHelper import *


def db_annotater_get_user_album_data(uid):
	"""This function get 

	:param uid: user id
	:type uid: int
	:returns: sensor type id in the sensortype table 
	"""
	print "====================="
	print "uid"
	print uid
	print "====================="
	albums 		= []
	album_dates	= {}
	if uid < 1:
		return None 
	else:
		# get all albums of a user
		albums_queryset = Album.objects.filter(user_id=uid).order_by('capture_date').values('id','capture_date', 'annotation','start_at', 'end_at')
		(latest_album_date, album_dates) 	= db_annotater_get_user_album_dates(albums_queryset)
		#albums			= db_annotater_get_user_albums(albums_queryset)
		if latest_album_date is not None:
			albums = db_annotater_get_latest_user_albums(latest_album_date)
	return (album_dates, albums)

def db_annotater_get_user_album_dates(albums_queryset):
	"""This function get all albums dates of a user

	:param 	uid: user id 
	:type 	uid: int 

	:returns: 
	"""

	# analyse the queryset of all albums of a user
	latest_date 	= ""#datetime.now().date()
	submit_dates	= []
	unsubmit_dates	= []
	latest_album	= None 
	for album_date in albums_queryset:
		if album_date['annotation'] is True:
			new_date = get_date_dash_d_m_y(album_date['capture_date'])
			submit_dates.append(new_date)
		else:
			new_date = get_date_dash_d_m_y(album_date['capture_date'])
			unsubmit_dates.append(new_date)
	if len(albums_queryset) > 0:
		latest_album= albums_queryset.reverse()[0]
		latest_date = latest_album['capture_date']
		latest_date = get_date_dash_d_m_y(latest_date)
		latest_album_id = latest_album['id']
	album_dates = {'ld':latest_date,'s':submit_dates,'u':unsubmit_dates} 
	return (latest_album,album_dates)

def db_annotater_get_date_album(selected_date,uid):
	"""This function get all albums for one selected date
	TODO: 
	:param 	uid: user id 
	:type 	uid: int 

	:returns: 
	"""
	#print selected_date
	#log = 1/None
	selected_date 	= date_picker_get_date(selected_date)
	albums_queryset = Album.objects.filter(user_id=uid,capture_date=selected_date).order_by('capture_date').values('id','capture_date', 'annotation','start_at', 'end_at')
	album_date 		= albums_queryset[0]

	album_id 	= album_date['id']
	start_at	= album_date['start_at']
	end_at		= album_date['end_at']
	(hours, mins, secs) = get_time_diff_h_m_s(start_at, end_at)
	wear_time 	= [{"hours":str(hours),"minutes":str(mins)}]
	album_id 	= album_date['id']
	if album_date['annotation'] is True:
		submitted = "Yes"
	else:
		submitted = "No"
	capture_date = get_date_dash_d_m_y(album_date['capture_date'])
	# get images
	images 		= db_annotater_get_album_images(album_id)

	images 		= db_annotater_get_album_images(album_id)
	one_album 	= {"wearTime" : wear_time, \
				"submitted" : submitted, \
				"date"      : capture_date, \
				"images"    : images}
	return one_album

def db_annotater_get_latest_user_albums(album_date):
	"""This function get all albums dates of a user
	TODO: optimize the process to give it a short 
	:param 	uid: user id 
	:type 	uid: int 

	:returns: 
	"""
	start_at	= album_date['start_at']
	end_at		= album_date['end_at']
	(hours, mins, secs) = get_time_diff_h_m_s(start_at, end_at)
	wear_time 	= [{"hours":str(hours),"minutes":str(mins)}]
	album_id 	= album_date['id']
	if album_date['annotation'] is True:
		submitted = "Yes"
	else:
		submitted = "No"
	capture_date = get_date_dash_d_m_y(album_date['capture_date'])
	# get images
	images 		= db_annotater_get_album_images(album_id)
	one_album 	= {"wearTime" : wear_time, \
				"submitted" : submitted, \
				"date"      : capture_date, \
				"images"    : images}
	return [one_album]

def db_annotater_get_user_albums(albums_queryset):
	"""This function get all albums dates of a user

	:param 	uid: user id 
	:type 	uid: int 

	:returns: 
	"""

	# analyse the queryset of all albums of a user
	albums			= []

	latest_date 	= ""
	print "db_annotater_get_user_albums"
	for album_date in albums_queryset:
		start_at	= album_date['start_at']
		end_at		= album_date['end_at']
		(hours, mins, secs) = get_time_diff_h_m_s(start_at, end_at)
		wear_time 	= [{"hours":str(hours),"minutes":str(mins)}]
		album_id 	= album_date['id']
		if album_date['annotation'] is True:
			submitted = "Yes"
		else:
			submitted = "No"
		capture_date = get_date_dash_d_m_y(album_date['capture_date'])
		# get images

		images = db_annotater_get_album_images(album_id)
		one_album = {"wearTime"	: wear_time, \
					"submitted"	: submitted, \
					"date"		: capture_date, \
					"images"	: images}
		albums.append(one_album)
	return albums

def db_annotater_get_album_images(album_id):
	"""This function get all images of a user of a day

	:param 	album_id: 
	:type 	album_id: date 
	:returns: 
	"""
	images			= []
	images_queryset	= Picture.objects.filter(album_id=album_id, visible=True).values('id', 'capture_at', 'file')
	for img in images_queryset:
		images.append({'time':str(img['capture_at'].time()), 'src':img['file'], 'imgId':img['id']})
	new_images = sorted(images, key=lambda k: k['src']) 
	return new_images 

def db_get_annotation_terms(uid):
	"""This function get all annotation terms from the database and return it to the interface

	:param 	uid: user id 
	:type 	uid: int  
	:returns: dictionary of annotation terms 
	"""
	terms = {}
	terms_queryset = AnnotationTerm.objects.filter(Q(private=False) | Q(user=uid)).values('concept', 'category')
	# all public terms
	for term_attr in terms_queryset:
		# get attributes
		category 	= str(term_attr['category']).strip()
		concept		= str(term_attr['concept']).strip()
		if category in terms:
			terms_list = terms[category] # here is the refer, not a copy
			terms_list.append(concept)
		else:
			terms[category] = [concept]
	return terms

def db_delete_one_image(imgId):
	"""This function deletes one image from the database
		as mark visible = False

	:param 	imgId: image id 
	:type 	imgId: int  
	:returns: 
	"""
	print "delete one image from database: "+ str(imgId)
	image			= Picture.objects.get(pk=imgId)
	image.visible 	= False
	image.save() 

def db_get_annotation_assignment():
	"""This function get all annotation assignment for adminstrater
		Get all users in the user table, with group annotater and subjects respectively

	:param 	: 
	:type 	:   
	:returns: dictionary of annotation terms 
	"""
	terms = {}
	terms_queryset = AnnotationTerm.objects.all()
	for term_attr in terms_queryset:
		# get attributes
		category 	= str(term_attr['category']).strip()
		concept		= str(term_attr['concept']).strip()
		if category in terms:
			terms_list = terms[category] # here is the refer, not a copy
			terms_list.append(concept)
		else:
			terms[category] = [concept]
	return terms


def db_annotater_get_user_annotatees(uid):
	"""This function return all annotatees list for user uid 

	:param uid: user id
	:type uid: int
	:returns: list of annotatees, with name and id 
	"""
	annotatees = AnnotationTask.objects.filter(annotator_id=uid).values('subject','no_album', 'finished')
	return annotatees 


def db_annotater_insert_user_annotation(uid, image_ids, annotation_terms):
	"""This function saves all user annotation from the interface into the database

	:param uid: user id
	:type uid: int
	:param annotations: all annotations made by user uid
	:type annotations: list
	:returns: list of annotatees, with name and id 
	"""
	try:
		for iid in image_ids:
			for term in annotation_terms:
				aid = AnnotationTerm.objects.filter(concept=term)[0].id
				#print aid
				#print "---aid-----"
				annotation_action = AnnotationAction(annotator=User(id=uid), image=Picture(id=iid), concept=AnnotationTerm(id=aid))
				annotation_action.save()
	except ValidationError:
		print "ValidationError"#to be modified
	return  

def db_annotater_insert_annotation_term(uid, concept, category):
	"""This function saves all user annotation from the interface into the database

	:param uid: user id
	:type uid: int
	:param annotations: all annotations made by user uid
	:type annotations: list
	:returns: list of annotatees, with name and id 
	"""
	try:
		annotation_term= AnnotationTerm(user=User(id=uid), concept=concept, category=category,private=True)
		annotation_term.save()
	except ValidationError:
		print "ValidationError"#to be modified
	return  

def create_annotationaction_object(uid, capture_at, imagename, annotation_concept):
	path = imagename_2_path(imagename, uid, capture_at)
	picture = Picture.objects.get(file=path)
	concept = AnnotationTerm.objects.get(concept=annotation_concept)
	annotation_action = AnnotationAction(annotator=User(id=uid), image=Picture(id=iid), concept=AnnotationTerm(id=aid))
	return annotation_action
	

def utils_batch_import_annotation():
	"""This function batch insert all contents in a sensor file into sensor database table
	
	:param  sensor_list: file path 
	:type   file_path: string
	:returns: datetime.date
	"""
	try:
		AnnotationAction.objects.bulk_create(annotation_action_list)
	except IntegrityError:
		print "IntegrityError in utils_batch_import_annotation"
