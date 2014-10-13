#! models.py
import os
import sys

new_path = sys.path[0]+'/lib/common'
if new_path not in sys.path:
	sys.path.append(new_path)

#print "-----------------------------------------------------------------"
#print sys.path
#print "-----------------------------------------------------------------"
from django.db import models
from django.contrib.auth.models import User
from files import MediaFileSystemStorage
from files import OverwriteStorage


def img_file_url(instance, filename):
	url = "img/user_{id}/{y}/{m}/{d}/{file}".format(id=instance.user.id,y=instance.year,m=instance.month,d=instance.day,file=filename)
	return url

def sensor_file_url(instance, filename):
	print '========instance.capture_at========'
	print instance.capture_at
	print str(instance.capture_at)
	url = "sensor/user_{id}/{file}".format(id=instance.user.id,file='sensor_'+str(instance.capture_at)+'.csv')
	return url
	
def json_sensor_file_url(instance, filename):
	print '========instance.capture_at========'
	print instance.capture_at
	print str(instance.capture_at)
	url = "sensorjson/user_{id}/{file}".format(id=instance.user.id,file='sensorjson_'+str(instance.capture_at)+'.json')
	return url
	
# sensor types 
# independant
class SensorType(models.Model):
	name		= models.CharField(max_length=100,default='sensor_type',unique=True)
	abbreviation= models.CharField(max_length=10,default='st',unique=True,db_index=True)

	def __unicode__(self):
		return u'%s' % (self.name)

# device types 
class DeviceType(models.Model):
	name		= models.CharField(max_length=100,default='device_name',unique=True,db_index=True)
	add_by_user = models.ForeignKey(User, unique=False)
	abbreviation= models.CharField(max_length=10,default='st',unique=True)

	def __unicode__(self):
		return u'%s' % (self.name)

# one user's data for one day is an album
# duration_sec= models.IntegerField()
class Album(models.Model):
	user 		= models.ForeignKey(User, unique=False)
	device 		= models.ForeignKey(DeviceType, unique=False)
	start_at  	= models.DateTimeField()
	end_at  	= models.DateTimeField()
	capture_date= models.DateField()
	annotation	= models.BooleanField(default=False)
	uploaded_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		index_together = [
							['user', 'capture_date'],
						]
# the following is to save file into the current date folder
# file 			= models.FileField(upload_to='img/%Y/%m/%d')
# the following is to save files into a specified folder 
# use the custom storage class fo the FileField
# for that authenticated user
# unique together ensures the same image of the same user wont be stored twice
class Picture(models.Model):
	user 		= models.ForeignKey(User, unique=False)
	album 		= models.ForeignKey(Album, unique=False, null=True)
	#file 		= models.FileField(upload_to=img_file_url, storage=MediaFileSystemStorage())
	file 		= models.FileField(upload_to=img_file_url)
	resized		= models.BooleanField(default=False)
	year		= models.CharField(max_length=4,default='2014')
	month		= models.CharField(max_length=2,default='01')
	day			= models.CharField(max_length=2,default='01')
	capture_at  = models.DateTimeField(auto_now_add=False)
	uploaded_at = models.DateTimeField(auto_now_add=True)
	updated_at  = models.DateTimeField(auto_now=True)
	visible		= models.BooleanField(default=True)
	codable		= models.BooleanField(default=True)

	class Meta:
		unique_together = ('user', 'file',)
		index_together = [
							['user', 'album', 'file'],
						]

"""
	def save(self, *args, **kwargs):
		if not self.pk:  # file is new
			md5 = hashlib.md5()
			for chunk in self.orig_file.chunks():
				md5.update(chunk)
			self.md5sum = md5.hexdigest()
		super(Picture, self).save(*args, **kwargs)
"""

# a sensor has to belong to a image
# sensor file will be saved in the database
class Sensor(models.Model):
	user 		= models.ForeignKey(User)
	sensor_type = models.ForeignKey(SensorType)
	value		= models.CharField(max_length=100,default='0')
	capture_at  = models.DateTimeField()
	uploaded_at = models.DateTimeField(auto_now_add=True)
	updated_at  = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = ('user', 'sensor_type','capture_at')


# a json sensor for one day only
# stores all sensor files of one users' one day sensor
class SensorJsonFile(models.Model):
	user 		= models.ForeignKey(User, unique=False)
	file 		= models.FileField(upload_to=json_sensor_file_url)
	type 		= models.ForeignKey(SensorType, unique=False, null=False)
	capture_at  = models.DateTimeField()
	uploaded_at = models.DateTimeField(auto_now_add=True)
	updated_at  = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = ('user', 'file')

# raw sensor file
# independant
# need to know what kind of device took the data
class SensorFile(models.Model):
	user 		= models.ForeignKey(User, unique=False)
	file 		= models.FileField(upload_to=sensor_file_url,storage=OverwriteStorage())
	capture_at	= models.DateTimeField()
	uploaded_at = models.DateTimeField(auto_now_add=True)
	updated_at  = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = ('user', 'file')

# raw sensor file
# independant
# Try not to use funf, but to develop our own software and have a full control of database and data capture, work with Zhengwei Qiu
class FunfSensorFile(models.Model):
	user 		= models.ForeignKey(User, unique=False)
	file 		= models.FileField(upload_to=sensor_file_url)
	capture_at	= models.DateTimeField()
	uploaded_at = models.DateTimeField(auto_now_add=True)
	updated_at  = models.DateTimeField(auto_now=True)
