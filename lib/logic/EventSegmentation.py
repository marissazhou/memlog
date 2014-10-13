"""
	Event Segmentation class. This is the main class that conduct event segmentation for lifelogging system 
	It does three main things:
		1. Get Sensor Data From DB 
		2. Segment Sensory Data into Events 
		3. Insert into DB with Event info 

.. module:: EventSegmentation socket is a module, containing the class EventSegmentation. 
   :platform: Ubuntu Unix
   :synopsis: A module for 

.. moduleauthor:: Lijuan Marissa Zhou <marissa.zhou.cn@gmail.com>
.. moduletime:: 2014-01-26 
"""
import os,sys
from pylab import *
from matplotlib import pyplot as plt
import re
import csv
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime, date, time
from dateutil import parser as dparser

# Self defined module in this project
from common import *

from common.calculation import *
from common.utils import *
from common.memlog_settings import *
from common.image import *

# import models for saving data
os.environ["DJANGO_SETTINGS_MODULE"] = "sensecam_browser.settings"
from eventseg.models import Event 
from eventseg.models import EventImage 
from fileuploader.models import Picture 
from django.contrib.auth.models import User


class EventSegmentation():

	"""
	all are public variables and can be called through self. 
	"""
	images_number 			= 0
	images_upload_number 	= 0
	sensor_path				= "/home/marissa/Documents/Autographer_lifelog/marissa_lifelog/2013/12/image_table.txt"
	current_event_pictures	= []
	valid_dates				= [] # The dates that contains data 
	events					= []
	sensors					= []
	sensor_loaded_data		= []
	current_event			= {} 
	user_id					= 1 

	def __init__(self, user_id, sensor_path):
		"""This function initializes an EventSegmentation object  
		:param:
		:returns: 
		"""
		self.sensor_path = sensor_path
		self.user_id		= user_id 
		self.read_sensor() # 
		self.autographer_segment() # 

	#################################################
	# 												# 
	#################################################
	def autographer_segment(self):#
		"""This function segments one upload data into differnt events 
            algorithm 1: use accelerometer data
            algorithm 2: use accelerometer data
		:param :
		:type :
		:returns: a list of events, each element is a dict with events info 
		:raises: 
		"""
		pre_acc_combined 	= 0
		# in Autographer pic_num is the same as sensor_num, but in sensecam it is different
		pic_num				= 0 
		sensor_num			= 0 
		key_frame			= '' 
		start_time			= '' # event start time 
		end_time			= '' # event end time 
		images			= [] # picture list for the current event 
		time_list			= [] # time list for the current event 
		taken_time_list		= [] 
		current_event		= {} 
		current_date		= None 

		if len(self.sensors) > 0:
			pre_acc_combined= square_root(self.sensors[0][5:8])
			current_time    = autographer_string_to_time(self.sensors[0][0])
			current_date    = current_time.date()
			print "###############################"
			
			LATEST_DATE		= current_date
			self.initiate_new_event(current_time)
		else:
			print "There is no sensor data"
			return
		# 
		counter = 0 
		for sensor in self.sensors:
			counter += 1
			# get picture id in the table to store in database
			pic_id = 1
			# get picture address 
			pic_address = get_pic_address(sensor[1], 0) #get picture address according picture name
			images.append({"id":pic_id,"address":pic_address})

			new_time    = autographer_string_to_time(sensor[0])
			new_date	= new_time.date()
			if is_same_date(new_date,current_date): # same date
				# to-do: should be start a new event, these can be implemented and experimented by different methods
				if counter%200 == 0: # a new event starts
					print "counter 200"
					if pic_num != 0:
						# 
						key_frame 					= get_key_frame_for_event(images)
						current_event["pic_num"] 	= len(images)
						current_event["keyframe"] 	= key_frame
						# record current event
						self.events.append(current_event)
						event = self.record_current_event()
						self.record_current_event_images(event, images)
						self.initiate_new_event(new_time)
					else:
						# log a empty event
						print "An empty event"
				else: # should be in the same event
					pic_num += 1
					sensor_num += 1
					# get picture id in the table
					pic_id = 1
				time_list.append(sensor[0])	
			else: # a new day a new event
				# store the current event
				if pic_num == 0:
					continue
				elif sensor_num != 0:# concatrate with last event
					self.events.append(current_event)
					event = self.record_current_event()
					self.record_current_event_images(event, images)
					self.initiate_new_event(new_time)
				# initiate a new event
				current_date = new_date 
				self.initiate_new_event(new_time)
				if current_date > LATEST_DATE: # LATEST_DATE is defined in common/settings
					LATEST_DATE = current_date
		# the last event in the sensor file
		if pic_num != 0:
			key_frame = get_key_frame_for_event(images) # gets full address of the picture	
			current_event["pic_num"] 	= len(images)
			current_event["keyframe"] 	= key_frame
			# record current event
			self.events.append(current_event)
			event = self.record_current_event()
			self.record_current_event_images(self.event, images)

		# to-do: write into log db.table
		print counter
		print len(self.events)
		write_log_user_interaction(self.user_id, 1, "log message")

	def record_current_event(self):#
		"""This function records an event into an Event object 
		after model.save(), the object will have an actual id

		:param current_event: the Event dict to store the current event information 
		:type current_event: dict 

		:returns: 
		:raises: 
		"""
		#call event in models
		#To save an object back to the database, call save()
		#us = User.objects.get(id=self.user_id)
		us = User.objects.get(id=1)
		sa = self.current_event["start_at"]
		ea = self.current_event["end_at"]
		lo = self.current_event["location"]
		sn = self.current_event["sensor_num"]
		pn = self.current_event["pic_num"]
		kf = self.current_event["keyframe"]
		sh = self.current_event["shared"]
		event = Event(start_at=sa,end_at=ea,user=us,location=lo,sensor_num=sn,pic_num=pn,keyframe=kf,shared=False,favourite=False)
		event.save()
		self.events.append(self.current_event) # events will be used to representing latest events in the interface
		return event

	def record_current_event_images(self, event, images):#
		"""This function records an event into an Event object 
		after model.save(), the object will have an actual id

		:param current_event: the Event dict to store the current event information 
		:type current_event: dict 

		--to do--
		if image is not found in the image table

		:returns: 
		:raises: 
		"""
		#call event in models
		#To save an object back to the database, call save()
		for pic in images:
			img 	= Picture.objects.get(id=pic["id"])
			evt 	= event
			event_image = EventImage(image=img, event=evt)
			event_image.save()
		return 

	def initiate_new_event(self, sample_time):#
		"""This function records an event into an Event object 
		:param sample_time: sample time for the current sensor
		:type sample_time: Date

		:returns: 
		:raises: 
		"""
		self.current_event['start_at'] 	= sample_time 
		self.current_event['end_at'] 	= sample_time 
		self.current_event['location'] 	= "" 
		self.current_event['sensor_num'] = 0 
		self.current_event['pic_num'] 	= 0 
		self.current_event['keyframe'] 	= "" 
		self.current_event['shared'] 	= False
		self.current_event['favourite'] 	= False 

	def get_key_frame(self, images):
		"""This function returns the key frame from a sequence of pictures 
		:param images: list of pictures 
		:type images: list

		:returns: key frame image full address 
		:raises: 
		"""
		for pic in images: #
			if pic["address"].find('.JPG') > 0:
				return pic["address"] 
		return 

	def process_sensor_line_autographer(self, sensor, line):#
		"""This function read current line of sensor file taken by Autographer
		:param sensor: sensor line
		:type sensor: [] 

		:returns: 
		:raises: 
		"""
		return 

	def process_sensor_line_sensecam(self, sensor, line):#
		"""This function reads current line of sensor data and put into Sensor object
		:param sensor: sensor line
		:type sensor: [] 

		:returns: 
		:raises: 
		"""
		if line[0] is "ACC": #
			sensor.set_acc_x(line[2])
			sensor.set_acc_y(line[3])
			sensor.set_acc_z(line[4])
			return
		elif line[0] is "PIR": #
			sensor.set_pir_manipulated(line[2])
			return
		elif line[0] is "TMP": #
			sensor.set_temperature(line[2])
			return
		elif line[0] is "CLR": #
			sensor.set_white_val(line[2])
			return
		elif line[0] is "MAG": #
			sensor.set_mag_x(line[2])
			sensor.set_mag_y(line[3])
			sensor.set_mag_z(line[4])
			return
		elif line[0] is "CAM": #
			sensor.set_image_name(line[2])
			sensor.set_trigger_code(line[3])
			return
		else: #
			return

	def get_address(self, orgn):#
		"""This function records an event into an Event object 
		:param sample_time: sample time for the current sensor
		:type sample_time: Date

		:returns: 
		:raises: 
		"""
		statement() #
		details = orgn.split('\/') #
		address = "" 
		return address 

	def get_event_list_day(self, ):#
		"""This function records an event into an Event object 
		:param sample_time: sample time for the current sensor
		:type sample_time: Date

		:returns: 
		:raises: 
		"""
		statement() #
		return 

	def get_event_detailed_images(self, index):#
		"""This function records an event into an Event object 
		:param sample_time: sample time for the current sensor
		:type sample_time: Date

		:returns: 
		:raises: 
		"""
		return #new List(events) #

	def read_sensor(self):#
		"""This function reads sensor file in Autographer dataset 
			Solution 1: We do hope the sensor file can be split into different dates same as images 
			Solution 2: when people upload, these will be segmented into events instantly  
			Here how to read a csv file can be improved by using converter and bytedate2num
			Notice: 
			1. The first two lines of the csv file is not sensor data but header
			2. 

		:param path: path of the sensor file
		:type path: string 

		:returns: an exposure object 
		:raises: an exception 
		"""
		with open(self.sensor_path, 'rb') as f:
			reader 	= csv.reader(f)
			counter = 0
			for row in reader:
				if counter < 2:
					counter = counter + 1
					continue
#(dt,img,sz,typ,p,accx,accy,accz,magx,magy,magz, \
#				 red,green,blue,lum,tem,g,lat,lon,alt,gs,herr,Verr,exp, \
#				 gain,rbal,gbal,bbal,xor,yor,zor,stags,tags) = row
#print row
				self.sensors.append(row)
		print len(self.sensors)
		return 

	def update_sensor_array(event_id, start, end):
		'''This function updates the sensor array 
		
		:param event_id: time 
		:type event_id: string 
		:param start: time 
		:type start: int 
		:param end: time 
		:type end: int 
		:returns: 
		'''
		i = start
		for i in range(start, end+1):
			sensors[i].set_event_id(event_id)


	def update_event_array(event_id, i):
		'''This function updates the sensor array 
		
		:param event_id: time 
		:type event_id: string 
		:param i: time 
		:type i: int 
		:returns: 
		'''
		event[i].set_event_id(event_id)

	def concate_events(event_1, event_2):
		'''This function updates the sensor array 
		
		:param event_1: event object 
		:type event_1: Event 
		:param event_2:  event object 
		:type event_2: Event 
		:param i: time 
		:type i: int 
		:returns: 
		'''
		event_1.set_end_time(event_2.get_end_time())
		event_1.set_time_list(event_1.get_time_list().concat(event_2.get_time_list()))
		event_1.set_end_time(event_1.get_images().concat(event_2.get_images()))
		event_1.set_pic_num(event_1.get_pic_num()+event_2.get_pic_num())
		event_1.set_sensor_num(event_1.get_sensor_num() + event_2.get_sensor_num())
		return event_1

