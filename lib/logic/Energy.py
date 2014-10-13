"""
	Energy expenditure estimation from accelerometer enabled android smartphones
	It does three main things:
		1. Get median number for a length of n to remove any abnormal noise spikes produces by the accelerometer
		2. Gravitiy filter to remove the gravitational acceleration and return accelerometer due to movement
		3. Diff to abastract information from array of acceleration values within one minute, return one single number to represent the activities happen in one particular direction
		
	Position	a0			a1			a2			a3			a4
	Back-hip	-19.38725	0.0221735	0.2069136	0.0097913	0.0850542
	Chest		-17.68498	0.0233162	0.182277	0.0057937	0.0788557
	Right-arm	-14.07957	0.0173166	0.1825754	0.0539856	0.0417018
	Front-hip	-14.83626	0.0210675	0.1886483	0.035059	0.0524134

.. module:: Energy expenditure estimation 
   :platform: Ubuntu Unix
   :synopsis: A module for energy expenditure estimation 

.. moduleauthor:: Lijuan Marissa Zhou <marissa.zhou.cn@gmail.com>
.. moduletime:: 2014-02-11
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
from common.settings import *
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
	ALPHA			= 0.8

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
	def calculate_energy(self, acc_xs, acc_ys, acc_zs, age, weight, height):#
		"""This function calculates energy level 
		each array here contains acelerometer values within one minute
		For demonstration purpose, filtering process is donge every minute, 
		while as in reality, it is better to be done within a longer time period

		:param acc_xs: accelerometer x values
		:type acc_xs: list
		:param acc_ys: accelerometer y values
		:type acc_ys: list
		:param acc_zs: accelerometer z values
		:type acc_zs: list
		:param age: age of users, year 
		:type age: float 
		:param weight: weight, kg 
		:type weight: float 
		:param height: height, cm 
		:type height: float 
		:returns: energy in calorie 
		:raises: 
		"""
		record_num			= len(acc_xs) 
		x_values			= [] 
		y_values			= [] 
		z_values			= [] 
		acc_value			= 0
		ee_value			= 0

		# median filtering process
		x_values			= self.median_filter(acc_xs)
		y_values			= self.median_filter(acc_ys)
		z_values			= self.median_filter(acc_zs)

		# gravity filtering process
		x_values			= self.gravity_filter(x_values)
		y_values			= self.gravity_filter(y_values)
		z_values			= self.gravity_filter(z_values)

		# get difference 
		tx					= self.diff(x_values)
		ty					= self.diff(y_values)
		tz					= self.diff(z_values)
		
		acc_value			= math.sqrt(tx*ty, tx*tz, ty*tz)

		# parameters a0 to a4 depend on the postion of phone device,
		# if the position is unknown, average value is taken
		ee_value			= a0 + a1*acc_value + a2*age + a3*weight + a4*height

	def median_filter(self, acc):#
		"""This function removes abnormal noise spikes produced by the accelerometer

		:param acc: list of a sequence of accelerometer data 
		:type acc: list 

		:returns: median filtered accelerometer 
		:raises: 
		"""
		record_num			= len(acc) 
		new_acc				= [] 
		new_acc.append(acc[0])
		for i in range(1:record_num-1):
			new_acc[i] = np.median([acc[i-1], acc[i], acc[i+1]]) # get_median is a function in common module
		return new_acc

	def grivity_filter(self, acc):#
		"""This function removes the gravitational acceleration
		and return acceleration due to movement

		:param acc: results from the median_filter(raw_acc) 
		:type acc: list 

		:returns: gravitational acceleration reduced new acceleration value 
		:raises: 
		"""
		if len(acc<1):
			return None
		record_num			= len(acc) 
		new_acc				= [] 
		temp				= acc[0] 
		for i in range(1:record_num):
			temp			= self.ALPHA*temp + (1-self.ALPHA)*acc[i] # get_median is a function in common module
			new_acc			= acc[i] - temp
		return new_acc

	def diff_filter(self, acc):
		"""This function tries to abstract information from array of acceleration values within one minute
		returns one single number to represent the activities
		happen in one particular direction

		:param acc: result from the grivity_filter(acc) 
		:type acc: list 

		:returns: a float number of difference 
		:raises: 
		"""
		record_num			= len(acc) 
		new_acc				= sorted(acc) 
		result				= 0.0
		new_acc.append(acc[0])

		for i in range(1:record_num-1):
			result = result + new_cc[record_num-1-i] - new_acc[i]
		return result 

