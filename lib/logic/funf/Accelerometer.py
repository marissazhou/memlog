"""Accelerometer class. This class reads funf AccelerometerSensorProbe.csv file 
	Activities include:
		1. Walking
		2. Driving
		3. Standing Still

	It does three main things:
		1. Combines 3 dimensional accelerometer data 
		2. 
		3. 

	Features for acceleration data includes:
		1. mean
		2. standard deviation
		3. variance
		4. median

	Auxilary tools:
		1. pybrain

.. module:: logic 
   :platform: Ubuntu Unix
   :synopsis: A module for logic operations like event segmentation, automatic annotation generation, lifelogger profile modelling etc.

.. moduleauthor:: Lijuan Marissa Zhou <marissa.zhou.cn@gmail.com>
.. moduletime:: 2014-01-26 

"""
import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
from pylab import *
from matplotlib import pyplot as plt
import numpy as np


# math
import scipy
import scipy.stats as stats

class Accelerometer():
	"""
		
	"""

	accelerometerSensorProbeFilePath = None
	timestamp		= [] 
	acc_x = [] 
	acc_y = [] 
	acc_z = [] 

	def __init__(self, path):
		"""This function initializes an PrimeCoordinator object  
		:param:
		:returns: 
		"""
		self.accelerometerSensorProbeFilePath = path

	def get_features(self):
		"""This function returns all features of all acceleration data and store all features in a matrix
			features include:
			1. 10 x-axis 
			2. 10 y-axis 
			3. 10 z-axis 

		:param:
		:returns: 
		"""
		# mean
		mean_x = np.mean(self.acc_x)
		mean_y = np.mean(self.acc_y)
		mean_z = np.mean(self.acc_z)
		# stardard deviation
		sd_x = np.std(self.acc_x, axis=0)
		sd_y = np.std(self.acc_y, axis=0)
		sd_z = np.std(self.acc_z, axis=0)

	#################################################
	# 												# 
	#################################################
	def combine_accelerometer(self):#
		"""This function 

		:param exposure_id: id for exposures
		:type exposure_id: int
		:returns: an exposure object 
		:raises: an exception 
		"""
		return 

	def csv_read(self):
		"""This function read an accelerometer file of funf

		:param path: path of the file that it is saved after uploading
		:type path: string
		:returns: list of dict of time, x, y, z 
		"""

		path = self.accelerometerSensorProbeFilePath
		with open(path, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
			reader.next()
			for row in reader:
				dt = datetime.datetime.fromtimestamp(float(row[4]))
				self.timestamp.append(dt)
				self.acc_x.append(row[5])
				self.acc_y.append(row[6])
				self.acc_z.append(row[7])

	def plotting(self):
		"""
		"""
		counter = 0
		magnitude = []

		for i in range(len(self.acc_x)):
			tempZero = self.acc_x[i]
			tempOne = self.acc_y[i]
			tempTwo = self.acc_z[i]
			temp = (float(tempZero) ** 2) + (float(tempOne) ** 2) + (float(tempTwo) ** 2)
			magnitude.append(temp)
			counter += 1

		plt.plot(self.acc_x)
		plt.plot(self.acc_y)
		plt.plot(self.acc_z)
		plt.plot(magnitude)
		xlabel('reading number')
		ylabel('accelerometer')
		title('accelerometer')
		grid(True)

		show() #showing the data

