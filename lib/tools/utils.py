"""utils 
   This class 
.. module:: common 
   :platform: Ubuntu Unix
   :synopsis: A module for all type of mathematical operation needed for Prime model

.. moduleauthor:: Lijuan Marissa Zhou <marissa.zhou.cn@gmail.com>

"""

'''
	PACKAGES
'''
import sys
import json
import csv
import scipy
from threading import Thread
from datetime import datetime, date, time

'''
	MODELS
'''
#timeutil = __import__("/var/www/sensecam_browser/lib/common/timeutils")
sys.path.append("/var/www/sensecam_browser/lib/common")
print sys.path
from timeutils_tmp import *
#from db.DBHelper import DBHelper
from stringutils import *

'''
 	CONSTRAINTS	
'''

class AnnotationImporter():

	def __init__(self, init_annotation_file_path):
		"""This function move files from one place to another place 
		
		:param albums: directory address string 
		:type albums: string 
		:returns: file address list 
		"""
		self.annotation_file_path = init_annotation_file_path

	def start_import(self):
		"""This function move files from one place to another place 
		
		:param albums: directory address string 
		:type albums: string 
		:returns: file address list 
		"""
		annotations = []
		with open(self.annotation_file_path, 'rb') as csvfile:
			filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
			filereader.next()
			for row in filereader:
				username = row[0].split("_")[0].strip()
				imagename = row[1].split("\\")[-1].strip()
				capture_at = string_2_datetime(row[2])
				annotation_term = annotation_import_get_annotation(row[3])
				image_path = imagename_2_path(imagename, uid, capture_at)
				annotations.append([username,image_path,annotation_term])
		#DBHelper.insert_annotationactions(annotations)

class SensorImporter():

	def __init__(self, init_sensor_file_path):
		"""This function move files from one place to another place 
		
		:param albums: directory address string 
		:type albums: string 
		:returns: file address list 
		"""
		self.sensor_file_path = init_sensor_file_path

	def start_import(self):
		"""This function imports all sensor records from the old sensecam browser to MemLog System
		
		:returns: file address list 
		"""
		sensors = []
		with open(self.sensor_file_path, 'rb') as csvfile:
			filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
			filereader.next()
			for row in filereader:
				capture_at = string_2_datetime(row[2])
				print capture_at
				sensors.append([capture_at])
		#DBHelper.insert_sensors(sensors)
