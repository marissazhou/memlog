 # -*- coding:utf-8 -*-
"""Sensor class
.. module:: Sensor 
   :platform: Ubuntu Unix
   :synopsis: A module for conducting all database relavant manipulations.

.. moduleauthor:: Lijuan Marissa Zhou <marissa.zhou.cn@gmail.com>

"""
from sensecambrowsercore.models import *
from sensecambrowsercore.prime import *
from sensecambrowsercore.logic import *

from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

import unicodedata

class Sensor: 
	chunk_id        = 0
	white_val       = 0
	battery         = 0
	pir             = 0
	event_id        = 0
	acc_x           = 0.0
	acc_y           = 0.0
	acc_z           = 0.0
	mag_x           = 0.0
	mag_y           = 0.0
	mag_z           = 0.0
	fuel_x          = 0.0
	fuel_y          = 0.0
	fuel_z          = 0.0
	temperature     = 0.0
	acc_combined    = 0.0
	pir_manipulated = 0.0
	trigger_code    = ''
	image_name      = ''
	sample_time     = ''

	def init(self):
        """ This function initializes an instance of Sensor class	

		:param :
        :type : 
        :returns: date of sensor sample time 
        """
        acc_x           = 0.0
        acc_y           = 0.0
        acc_z           = 0.0
        mag_x           = 0.0
		mag_y           = 0.0
		mag_z           = 0.0
		fuel_x          = 0.0
		fuel_y          = 0.0
		fuel_z          = 0.0
		temperature     = 0.0
		acc_combined    = 0.0
		pir_manipulated = 0.0
		trigger_code    = ''
		image_name      = ''
		sample_time     = ''

	#for SenseCam
	def sensor_reader_sc(chunkId,sampleTime,accX,accY,accZ,magX,magY,magZ,whiteVal,battery,temperature,pir,trigger_code,imageName):
        """ This function returns chunckId of current chuck id

        :param ele: An array to be sorted
        :type ele: array 
        :returns: void 
        """
		#this.chunkId = chunkId
		#this.sampleTime = sampleTime
		
	#for Vicon Renue
	def sensor_reader_vr(chunkId,sampleTime):
        """ This function returns chunckId of current chuck id

        :param chunkId: chunk id
        :type chunkId: int
        :param sampleTime: sample time of sensor
        :type sampleTime: date 
        :returns: void 
        """
		this.chunkId = chunkId;
		
	def get_raw_acc_combined(isVR):
        """ This function returns combined accelerometer data 

        :param isVR: is vicon revue
        :type isVR: boolean 
        :returns: combined accelerometer 
        """
		num = 0
		num = math.sqrt(Math.pow(StandCalculation.getSignedInt(self.acc_x,isVR),2)+Math.pow(StandCalculation.getSignedInt(self.acc_y,isVR),2)+Math.pow(StandCalculation.getSignedInt(self.acc_z,isVR),2));
		return num
	
	def get_date():
        """ This function returns date of the sample time	

        :param :
        :type : 
        :returns: date of sensor sample time 
        """
		arr = self.sample_time.split("\/")
		return new Date(arr[0],arr[1]-1,arr[2].split(" ")[0])

	def set_sample_time(sample_time):
        """ This function returns date of the sample time	

        :param :
        :type : 
        :returns: date of sensor sample time 
        """
		self.sample_time = sample_time
		

	def get_sample_time():
   		""" This function returns date of the sample time	

       	:param :
        :type : 
        :returns: date of sensor sample time 
        """
		return self.sample_time
