"""dabatabase manipulation class
.. module:: healthHelper
   :platform: Ubuntu Unix
   :synopsis: A module for conducting all database annotater.

.. moduleauthor:: Lijuan Marissa Zhou <marissa.zhou.cn@gmail.com>
.. copyright:: copyright reserved 

"""
import unicodedata
from datetime import datetime
from django.utils.dateparse import parse_datetime

from utils import *
from time import gmtime, strftime

from django.core.exceptions import ValidationError

from health.models import *
from fileuploader.models import *
from django.db.models import Q 


def db_get_daily_activities(uid, cur_date):
	"""This function get 

	:param uid: user id
	:type uid: int
	:param cur_date: current date
	:type cur_date: datetime.date
	:returns: sensor type id in the sensortype table 
	"""
	str_date = str(cur_date.date())
	s1 			= str(cur_date.date())+' 00:00:00' # start time
	s2 			= str(cur_date.date())+' 23:59:59' # end time, together covers 1 day
	n1 			= parse_datetime(s1) # naive object
	n2 			= parse_datetime(s2)
	aware_start_time 	= la.localize(n1) # aware object
	aware_end_time 		= la.localize(n2)

	if uid < 1:
		return None
	else:
		# get all activities of a user of one day
		activities = PhysicalActivity.objects.filter(user_id=uid, start_time__range=(aware_start_time, aware_end_time)).values('id', 'start_time','end_time', 'PhyscialActivityType__name')
	return activities

def db_get_all_daily_activities(uid):
	"""This function get 

	:param uid: user id
	:type uid: int
	:returns: sensor type id in the sensortype table 
	"""
	activities_queryset = PhysicalActivity.objects.filter(user_id=uid).values('id', 'start_time','end_time', 'pa_type__name').order_by('start_time')
	activities = db_get_activities(activities_queryset)
	# can choose to return different formats of activities
	return activities

def db_get_activities(activities_queryset):
	"""This function retrieves all activities from the queryset, and change return format to be 

	:param  activities_queryset: raw queryset of activities 
	:type   activities_queryset: list of dictionary

	:returns: 
	"""
	# analyse the queryset of all albums of a user
	activities = []

	if len(activities_queryset) < 1:
		return None

	cur_date     = activities_queryset[0]['start_time'].date() 
	one_day_activity = [] 
	for activities_date in activities_queryset:
		capture_date = activities_date['start_time'].date()
		if cur_date == capture_date:
			# save all actitivites of a day
			one_day_activity.append({"start_time": str(activities_date['start_time'].time()), \
					"end_time" 			: str(activities_date['end_time'].time()), \
                    "pa_type"    		: activities_date['pa_type__name']})
		else:
			# save current day's activities
			activities.append({"capture_date":get_date_dash_d_m_y(capture_date), "activities":one_day_activity})
			one_day_activity 	= [] 
			cur_date 			= capture_date
		# save the last date's activities
		activities.append({"capture_date":get_date_dash_d_m_y(cur_date), "activities":one_day_activity})
	return activities
