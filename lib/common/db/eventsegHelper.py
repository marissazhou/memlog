"""dabatabase manipulation class
.. module:: eventsegHelper
   :platform: Ubuntu Unix
   :synopsis: A module for conducting all database eventseg.

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
from eventseg.models import *
from django.db.models import Q 


def db_annotater_insert_user_annotation_event(uid, image_ids):
	"""This function saves one submit of annotation as one event
	1. get picture time as event time
	2. create Event object and save
	3. create EventImage objects and save

	:param uid: user id
	:type uid: int
	:param annotations: all annotations made by user uid
	:type annotations: list
	:returns: list of annotatees, with name and id 
	"""
	try:
		start_at 	= Picture.objects.get(id=image_ids[0]).capture_at
		event		= Event(user=User(id=uid), start_at=start_at)
		event.save()
		eid 		= event.id
		for iid in image_ids:
			eventImage = EventImage(image=Picture(id=iid),event=Event(id=eid))
			eventImage.save()
	except ValidationError:
		print "ValidationError"#to be modified
	return  

