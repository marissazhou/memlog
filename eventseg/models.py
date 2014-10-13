from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group 
from django.db.models.signals import post_save

from fileuploader.models import * 


# Event includes in the lifelogs
class Event(models.Model):
	user		= models.ForeignKey(User, default=1)
	start_at	= models.DateTimeField()
	end_at	    = models.DateTimeField()
	location	= models.CharField(max_length=1000)
	sensor_num  = models.IntegerField(default=0)
	pic_num     = models.IntegerField(default=0)
	keyframe    = models.CharField(max_length=1000)
	shared		= models.BooleanField(default=False)
	favourite	= models.BooleanField(default=False)
	created_at	= models.DateTimeField(auto_now_add=True)
	updated_at	= models.DateTimeField(auto_now=True)

	# this is useful for __getitem__
	def __unicode__(self):
		return self.keyframe

# Event includes in the lifelogs
class EventImage(models.Model):
	#image 		= models.ForeignKey('fileuploader.image', default=1)
	image 		= models.ForeignKey(Picture, default=1)
	event		= models.ForeignKey(Event, default=1)
