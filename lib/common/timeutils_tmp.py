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



def string_2_datetime(time_string):
	'''This function returns minute of events 
	
	:param dt: datetime object 
	:type dt: datetime 
	:returns: normal distribution 
	'''
	#time_format = '%Y/%m/%d %H:%M:%S'
	time_format_1 = '%m/%d/%Y %H:%M' # sensecam raw and uploaded
	time_format_2 = '%m/%d/%Y %H:%M:%S %p' # sensecam raw and uploaded
	time_format_3 = '%m/%d/%Y %H:%M:%S' # sensecam raw and uploaded
	time_format_4 = '%Y-%m-%d %H:%M:%S' # autographer raw time
	time_format_5 = '%Y-%m-%d %H:%M:%S.%f' # import annotation time
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
						return None
	if dt is not None:
		return dt
	else:
		return None

