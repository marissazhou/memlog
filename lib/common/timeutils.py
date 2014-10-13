"""timeutils 
   This class deals with all time relevent processing, including timezone switching, time format changing etc. 
.. module:: common 
   :platform: Ubuntu Unix
   :synopsis: A module for all type of mathematical operation needed for Prime model

.. moduleauthor:: Lijuan Marissa Zhou <marissa.zhou.cn@gmail.com>

"""
from datetime import datetime, date, time, timedelta
import pytz
from django.utils import timezone

#from settings import *
from django.conf import settings

'''
 	constants for distritubion types	
'''

settingstime_zone = pytz.timezone(settings.TIME_ZONE)


def get_datetime_timezone(dt):
	'''This function returns minute of events 
	
	:param dt: datetime object 
	:type dt: datetime 
	:returns: normal distribution 
	'''
	time = None
	tz = settingstime_zone 
	if tz:
		timezone.activate(tz)
		print "----------------"
		print dt 
		print dt.tzinfo
		print "----------------"
		#log = 1/None
		if dt.tzinfo == None:
			time = tz.localize(dt)
		else:
			time = dt 
	return time

def string_2_datetime(time_string):
	'''This function returns minute of events 
	
	:param dt: datetime object 
	:type dt: datetime 
	:returns: normal distribution 
	'''
	#time_format = '%Y/%m/%d %H:%M:%S'
	print time_string
	time_format_1 = '%m/%d/%Y %H:%M' # sensecam raw and uploaded
	time_format_2 = '%m/%d/%Y %H:%M:%S %p' # sensecam raw and uploaded
	time_format_3 = '%m/%d/%Y %H:%M:%S' # sensecam raw and uploaded 2012/05/19 06:31:42
	time_format_4 = '%Y-%m-%d %H:%M:%S' # autographer raw time
	time_format_5 = '%Y-%m-%d %H:%M:%S.%f' # import annotation time
	time_format_6 = '%Y/%m/%d %H:%M:%S' # sensecam raw and uploaded 2012/05/19 06:31:42
	dt = None
	#dt = datetime.strptime(time_string, time_format_SenseCam)
	try:
		dt = datetime.strptime(time_string, time_format_1)
	except ValueError:
		try:
			dt = datetime.strptime(time_string, time_format_2)
		except ValueError:
			try:
				dt = datetime.strptime(time_string, time_format_3)
			except ValueError:
				try:
					dt = datetime.strptime(time_string, time_format_4)
				except ValueError:
					try:
						dt = datetime.strptime(time_string, time_format_5)
					except ValueError:
						try:
							dt = datetime.strptime(time_string, time_format_6)
						except ValueError:
							return datetime.now()
	if dt is not None:
		return dt
	else:
		return None

def date_picker_get_date(time_string):
	'''This function returns minute of events 
	
	:param dt: datetime object 
	:type dt: datetime 
	:returns: normal distribution 
	'''
	time_format = '%d/%m/%Y'
	dt = datetime.strptime(time_string, time_format)
	date = dt.date()
	return date
