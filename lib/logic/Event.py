"""Event class. This is the class that contains the attributions of events 
	It does three main things:
		1. 
		2. 
		3. 
.. module:: EventSegmentator 
   :platform: Ubuntu Unix
   :synopsis: A module for operating all exposures compound or only, baseline or counterfactual.

.. moduleauthor:: Lijuan Marissa Zhou <marissa.zhou.cn@gmail.com>

"""
from sets import Set

import unicodedata

class Event():

	"""
		exposure objects, both for only ones and compound ones
	"""
	event_id        = 0 # int
	user_id         = 0 # int
	start_date      = ''
	start_time      = ''
	end_date        = ''
	end_time        = ''
	picture_list    = [] # array of pics in this event
	sensor_list     = []
	time_list       = []
	picture_number  = 0 # int, number of pictures in this event	
	sensor_number   = 0 # int, number of sensors in this event	
	key_frame       = ''
	sensor_start_id = 0 # int
	sensor_end_id   = 0 # int
	is_shared       = False # boolean
	is_favourite    = False # boolean

	def __init__(self):
    	"""This function initializes an PrimeCoordinator object  

   		:param:
   	 	:returns: 
   		"""
		DBHelper.initialize() #initiate dababase helper

	#################################################
	# outcomes					# 
	# Function names should be lowercase, with words separated by underscores as necessary to improve readability. mixedCase is allowed only in contexts where that's already the prevailing style (e.g. threading.py), to retain backwards compatibility.
	#################################################
	def get_data(self):#id in db
		""" This function returns date of event start time	

   		:param self: 
   		:type self:
   	 	:returns: 
   	 	:raises: 
    	"""
		arr = self.startTime.split("\/")
		return new Date(arr[0],arr[1]-1,arr[2].split(" ")[0])


	def get_date_para(self, time):
        """ This function returns date of the given time	

    	:param :
       	:type : 
       	:returns: date of sensor sample time 
        """
		arr = time.split("\/")
		return new Date(arr[0],arr[1]-1,arr[2].split(" ")[0])
