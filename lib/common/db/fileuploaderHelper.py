#!/usr/bin/env python
"""dabatabase manipulation class
.. module:: DBFileUploaderHelper
   :platform: Ubuntu Unix
   :synopsis: A module for conducting all database relavant manipulations.
   :ps: media with the same user and name will not be saved twice 

   
.. moduleauthor:: Lijuan Marissa Zhou <marissa.zhou.cn@gmail.com>
.. copyright:: copyright reserved 


For Autographer file in device:
	1. 
For SenseCam file in device:
	1. 
For Vicon file in device:
	1. 

For uploaded Autographer file:
	1. 

Shall I do this for all types of devices

For uploaded SenseCam file:
	1. create a folder named current timestamp;
	2. read files until find image.dat/sensor.csv file; 
	3. read image.dat/sensor.csv file to get the capture date 
	4. create a folder named that date
	5. save new files into that folder and new thread move all previous files into that folder 

	1. 	Solution 1: read files and save into a temparary folder until a csv file is found, then create a folder for that specific day and move all image files into that folder; or if csv file is missed, move all images into a not found 
		Solution 2: read all files into a current timestamp folder and save into a temparary folder until a csv file is found, then create a folder for that specific day and move all image files into that folder; or if csv file is missed, move all images into a not found 
	1. read sensor.csv file to get date

For uploaded Vicon file:
	1. 

Picture file names:
SenseCam 	- 00031075.JPG
Vicon		- 00011328.JPG -> 0_0_date_time.j
Autographer - B00000781_21I5I2_20140303_1200294.JPG

"""
import sys

from timeutils import *
from datetime import datetime as dt
from threading import Thread
from time import sleep
import _mysql
import MySQLdb as mdb
import unicodedata
from django.db import IntegrityError
from dateutil.tz import tzlocal
from xml.dom import minidom

from fileuploader.models import *
#from fileuploader.models import Picture 
#from fileuploader.models import SensorFile
#from fileuploader.models import Sensor
#from fileuploader.models import Album

"""
/home/marissa/Documents/Autographer_lifelog/raw_data/UCSD/DATA
"""
from files import * 
from memlog_settings import *
from utils import * 
from image import * 

"""
global variables
Not sure we can put it here, whether it will cause conflicts when there are multiple users upload at the same time.
"""
image_ids           = {}
sensor_file_path    = None
album_date          = None
album_start_time    = None
album_end_time      = None
cur_album           = None
images_to_resize    = [] #resize
# FLAG for tagging if files from the current device need to be stored in a temparory folder
flag_temp 			= False
is_finished			= False
temp_files			= [] # all files that are named without a timestamp are stored in this list, including sensor file from Autographer
days_count			= 0
temp_album_id		= None 
benchmark_start_image_upload = None
benchmark_start_sensor_upload = None
benchmark_start_analyze_sensor = None
benchmark_start_move = None
benchmark_start_resize = None
benchmark_finish = None


def fileuploader_thread(uid, files, device_type, finished):
	"""This function starts a new thread for one user to upload files at a time
		For one user's one upload, by default, it should be one capture of data, one thread is started for that user's upload.
	:param 			 uid: user id 
	:type 			 uid: int
	:param 			 files: files list
	:type 			 files: list
	:param device_type: device type, refer to utils.py file
	:type  device_type: int 

	:returns: None 
	"""
	global is_finished
	global benchmark_start_image_upload
	if benchmark_start_image_upload is None:
		benchmark_start_image_upload = datetime.now() 
	is_finished = finished

	#print "length of files in fileuploader_thread"
	#print len(files)
	#thread = Thread(target=db_fileuploader_save_files, args=(uid,files,device_type))
	#thread.start()
	db_fileuploader_save_files(uid,files,device_type)
	# Wait until the thread terminates.
	# Does it need to wait this thread to finish to continue, no, it does not 
	# thread.join()
	# print "thread fileuploader finished...exiting"


def db_fileuploader_get_sensor_type(abbr, sensorname):
	"""This function get sensor type according to their abbreviations

	:param 			 abbr: abbreviation
	:type 			 abbr: string 
	:param 			 files: files list
	:type 			 files: list
	:returns: sensor type id in the sensortype table 
	"""
	types = {}
	if abbr is not None:
		#types = SensorType.objects.filter(abbreviation=abbr).values('id')
		types = SensorType.objects.filter(abbreviation=abbr)
		print "types"
		print types
	elif sensorname is not None:
		types = SensorType.objects.filter(name=sensorname)
	type = types[0]
	return type 

def db_fileuploader_get_album(uid, album_date):
	"""This function get album id according to capture time 
	
	:param 			 uid: user id 
	:type 			 uid: int
	:param 	   date_info: 
	:type 	   date_info: datetime.date 
	:returns: sensor type id in the sensortype table 
	"""
	album = None 
	if album_date is not None:
		albums = Album.objects.filter(user_id=uid,capture_date=album_date)
		if len(albums) > 0:
			album = albums[0]
	return album 

def db_fileuploader_update_album_time(cur_album, start_time, end_time):
	"""This function updates end_time of an album 
	TODO: optimize the process to increase efficiency

	:param 		a_id: an album id 
	:type 		a_id: int 
	:param 	end_time: end time of an album 
	:type 	end_time: datetime.date 
	:returns: sensor type id in the sensortype table 
	"""
	#print "===========update endtime============="
	if end_time is not None:
		#print end_time
		value = Album.objects.filter(id=cur_album.id).update(start_at=start_time,end_at=end_time)
		#value = cur_album.update(end_at=end_time)
		#print value
		#cur_album.update(end_at=end_time)


def db_fileuploader_save_files(uid, files, device_type):
	"""This function saves all files from a request to the database and server local directory

	:param 		a_id: an album id 
	:type 		a_id: int 
	:param 	end_time: end time of an album 
	:type 	end_time: datetime.date 

	:returns: sensor type id in the sensortype table 
	"""
	global image_ids 
	global flag_temp
	global album_date
	global temp_album_id

	# uid 			= arg[0]
	# files 		= arg[1]
	# device_type	= arg[2]

	# print "===========update endtime============="
	# process files according to device types
	# TODO: this code can be more consise
	if files is not None:
		#print "*******************Device_type*****************"
		#print device_type
		#print "*******************Test*****************"
		#device_type = 2
		if device_type is DEVICE_TYPE_AUTOGRAPHER:
			device 		= DeviceType.objects.filter(name="autographer")[0]
			flag_temp 	= False
			#process_files(files, uid, device)
			process_files(files, uid, device_type, device)
		elif device_type is DEVICE_TYPE_SENSECAM:
			device 		= DeviceType.objects.filter(name="sensecam")[0]
			flag_temp 	= True
			process_files_s(files, uid, device_type, device)
		elif device_type is DEVICE_TYPE_VICONREVUE:
			device = DeviceType.objects.filter(name="viconrevue")[0]
			flag_temp 	= True
			process_files_s(files, uid, device_type, device)
		elif device_type is DEVICE_TYPE_SENSESEER:
			device = DeviceType.objects.filter(name="senseseer")[0]
			flag_temp 	= True
			process_files_s(files, uid, device_type, device)
		elif device_type is DEVICE_TYPE_NARRATIVE:
			device = DeviceType.objects.filter(name="narrative")[0]
			flag_temp 	= True
			process_files_s(files, uid, device_type, device)
		elif device_type is DEVICE_TYPE_FUNF:
			device = DeviceType.objects.filter(name="funf")[0]
			flag_temp 	= False
			process_files_f(files, uid, device_type, device)
		elif device_type is DEVICE_TYPE_AUTOGRAPHER_U:
			device = DeviceType.objects.filter(name="autographer_u")[0]
			flag_temp 	= False
			process_files(files, uid, device_type, device)
		elif device_type is DEVICE_TYPE_SENSECAM_U:
			device = DeviceType.objects.filter(name="sensecam_u")[0]
			flag_temp 	= True
			process_files_su(files, uid, device_type, device)
		elif device_type is DEVICE_TYPE_VICONREVUE_U:
			device = DeviceType.objects.filter(name="viconrevue_u")[0]
			flag_temp 	= True
			process_files_su(files, uid, device_type, device)
		elif device_type is DEVICE_TYPE_SENSESEER_U:
			device = DeviceType.objects.filter(name="senseseer_u")[0]
			flag_temp 	= True
			process_files_s(files, uid, device_type, device)
		elif device_type is DEVICE_TYPE_NARRATIVE_U:
			device = DeviceType.objects.filter(name="narrative_u")[0]
			flag_temp 	= True
			process_files_s(files, uid, device_type, device)
		elif device_type is DEVICE_TYPE_FUNF_U:
			device = DeviceType.objects.filter(name="funf_u")[0]
			flag_temp 	= False
			process_files_f(files, uid, device_type, device)

	# start a new thread to resize images to get thumbnails
	# one upload is finished
	# start to move files and analyze 
	if is_finished:
		date_info   = [album_date.year, album_date.month, album_date.day, 0,0,0]
		process_temp_files(date_info)
		# this means the files are currently saved in a temperory folder 
		if flag_temp:
			# analyze sensor file to get both date, time and sensor information
			# get a json format of information about the sensor here
			# uid here is for saving temporary data
			move_and_resize_files_thread(sensor_file_path,date_info,uid,device)
		else:
			resize_files_thread(sensor_file_path,date_info,uid)
	else:
		# one upload not finished
		print "one upload not finished"
	return

def process_temp_files(date_info):
	global temp_files

	for temp_file in temp_files:
		afile 	= temp_file["afile"]
		filename    = afile.name.lower()
		if '.txt' in filename:
			afile 	= temp_file["afile"]
			uid 	= temp_file["uid"]
			device_type = temp_file["device_type"]
			device	= temp_file["device"]
			save_sensor_file(afile, uid, date_info)

def resize_files_thread(sensor_file_path, date_info, uid):
	"""This function resize images, for Autographer, when files don't need to be moved. 
	the logic should be resize images after move and database update
	
	:param dir: directory address string 
	:type dir: string 
	:param extention: file type that is wanted to be retrieved 
	:type extention: string 
	:returns: file address list 
	"""
	#print "resize"
	#print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
	if sensor_file_path is None:
		print sensor_file_path
		return
	#print "++++++++move_files_thread+++++++++++++++"
	# print sys.path
	# this move_files is in utils
	# it is been weired that fuctions in files are not callable
	thread = Thread(target = resize_images, args = (sensor_file_path, date_info, uid))
	thread.start()
	# Wait for all of them to finish
	# Wait until the thread terminates.
	#thread.join()

def move_and_resize_files_thread(sensor_file_path, date_info, uid,device):
	"""This function move files from one place to another place 
	the logic should be resize images after move and database update
	
	:param dir: directory address string 
	:type dir: string 
	:param extention: file type that is wanted to be retrieved 
	:type extention: string 
	:returns: file address list 
	"""
	if sensor_file_path is None:
		return
	#print "++++++++move_files_thread+++++++++++++++"
	# print sys.path
	# this move_files is in utils
	# it is been weired that fuctions in files are not callable
	#move_and_resize(date_info, uid,device)
	thread = Thread(target = move_and_resize, args = (date_info, uid,device))
	thread.start()
	# Wait for all of them to finish
	# Wait until the thread terminates.
	#thread.join()

def resize_images(sensor_file_path, date_info, uid):
	""" This function processes all unuploaded sensecam files directly from sensecam devices, these sensecam files are not previously uploaded using sensecam software.

	:param 	capture_time: capture time of this file, only available for image files 
	:type 	capture_time: datetime.datetime 

	:return: None
	"""
	images = Picture.objects.filter(resized=False).values('file')
	#print images
	#log = 1/None
	resize_image_list(images)
	#resize_image_list(images)

	# update picture items set resized to be True
	Picture.objects.filter(resized=False).update(resized=True)

def move_and_resize(date_info, uid, device):
	""" This function processes all unuploaded sensecam files directly from sensecam devices, these sensecam files are not previously uploaded using sensecam software.

	:param 	capture_time: capture time of this file, only available for image files 
	:type 	capture_time: datetime.datetime 

	:return: None
	"""
	global sensor_file_path 
	global temp_album_id
	global benchmark_start_image_upload
	global benchmark_start_sensor_upload
	global benchmark_start_analyze_sensor
	global benchmark_start_move
	global benchmark_start_resize
	global benchmark_finish

	#print "in thread move_and_resize"
	sensor_file_path = os.path.join(settings.MEDIA_ROOT, sensor_file_path)
	#print sensor_file_path 
	benchmark_start_analyze_sensor = datetime.now()
	(albums,file_capture_date) = sensecam_analyze_sensor(sensor_file_path, uid)
	#print file_capture_date
	#print "---------albums after sensecam_analyze_sensor(sensor_file_path, uid)----"
	album_dates = albums.keys()
	album_ids = {}
	for album_date in album_dates:
		#print albums[album_date][0]
		start_time = albums[album_date][0]['time']
		end_time = albums[album_date][-1]['time']
		#insert new albums
		"""
		print "------album start time and end time---------------------"
		print start_time
		print end_time
		print "------------------------------------------------"
		"""
		cur_album = check_for_album(start_time, end_time, uid, device)
		album_ids[album_date] = cur_album.id
	#print album_ids
	#print albums
	# move temp files into their folders with caputure dates
	#print date_info
	benchmark_start_move = datetime.now()
	move_files(albums, album_ids, date_info, uid)
	# move sensor file 
	sensor_file_path = move_sensecam_sensor_file(file_capture_date, sensor_file_path)
	#print sensor_file_path 

	# resize
	benchmark_start_resize = datetime.now()
	images = Picture.objects.filter(resized=False).values('file')
	#print images
	#log = 1/None
	resize_image_list(images)

	# update picture items set resized to be True
	Picture.objects.filter(resized=False).update(resized=True)

	# remove temporary album
	print "remove temporary album"
	print temp_album_id
	#DBHelper.remove_empty_albums(temp_album_id)
	Album.objects.filter(id=temp_album_id).delete()
	benchmark_finish = datetime.now()
	print_benchmarks()

def print_benchmarks():
	"""
	"""
	global benchmark_start_image_upload
	global benchmark_start_sensor_upload
	global benchmark_start_analyze_sensor
	global benchmark_start_move
	global benchmark_start_resize
	global benchmark_finish

	print "##############	image_upload period 	#######"
	print (benchmark_start_sensor_upload-benchmark_start_image_upload)
	print "##############	sensor_upload period 	#######"
	print (benchmark_start_analyze_sensor-benchmark_start_sensor_upload)
	print "##############	sensor analyze period 	#######"
	print (benchmark_start_move	-	benchmark_start_analyze_sensor)
	print "##############	move period 	#######"
	print (benchmark_start_resize	-	benchmark_start_move)
	print "##############	resize period 	#######"
	print (benchmark_finish			-	benchmark_start_resize)

def process_files_s(files, uid, device_type, device):
	""" This function processes all unuploaded sensecam files directly from sensecam devices, these sensecam files are not previously uploaded using sensecam software.
	There are two types of files in this case:
		1. images in different subfolders, named like "H02/M0201/00020101.JPG"
		2. SENSOR.CSV

	For uploaded SenseCam file:
		1. create a folder named current timestamp;
		2. read files until find image.dat/sensor.csv file; 
		3. read image.dat/sensor.csv file to get the capture date 
		4. create a folder named that date
		5. save new files into that folder and new thread move all previous files into that folder 


	:param 	capture_time: capture time of this file, only available for image files 
	:type 	capture_time: datetime.datetime 

	:return: None
	"""
	# same as sensecam uploaded
	process_files_su(files, uid, device_type, device)

def process_files_su(files, uid, device_type, device):
	""" This function processes all uploaded sensecam files, these sensecam files are previously uploaded using sensecam software.
	There are three types of files in this case:
		1. images in one folder, named like "00034388.JPG"
		2. image.bat file
		3. SENSOR.CSV

	For uploaded SenseCam file:
		1. create a folder named current timestamp;
		2. read files until find image.dat/sensor.csv file; 
		3. read image.dat/sensor.csv file to get the capture date 
		4. create a folder named that date
		5. save new files into that folder and new thread move all previous files into that folder 
	:param 	capture_time: capture time of this file, only available for image files 
	:type 	capture_time: datetime.datetime 

	:return: None
	"""
	global image_ids 
	global album_date 
	global is_finished
	global sensor_file_path 
	global benchmark_start_sensor_upload

	#print "*********len(files) in process_files_su****************"
	#print len(files)
	#print "=========process_sensecam_file========="

	"""
	this includes two steps:
	1. save all files into a temporary folder
	2. check if all files finished, move all files from the temporary folder to their time-tagged folder
	"""

	now_dt	    = datetime.now() 
	date_info 	= [now_dt.year, now_dt.month, now_dt.day, now_dt.hour, now_dt.minute, now_dt.second]
	album_date 	= now_dt

	for afile in files:
		file_saved_path = ''
		filename 		= afile.name
		#print filename
		# date_info = [year, month, day, hour, minute, second]
		# can not get this date info until sensor file is uploaded
		filename 	= filename.lower()
		if '.csv' in filename:
			#new_file= SensorFile(file=afile,user=User(id=uid),capture_at=album_date)
			#new_file.save()
			#print "=========save and analyze csv file========="
			benchmark_start_sensor_upload = datetime.now()
			save_sensor_file(afile, uid, date_info)
		elif '.dat' in filename:
			# here all files are stored in a temp folder at first until there is a image.
			#print "=========dat file========="
			#print "=========ingore dat file========="
			#save_dat_file(afile, uid, date_info)
			print ""
		elif '.jpg' in filename:
			try:
				save_image(afile, uid, date_info, device, device_type)
			#return image_path	
			except IntegrityError:
				print "IntegrityError in save_image"
				# insert into interaction log



def update_image_file_addresses(addresses):
	""" This function updates all image addresses in the database image table
		for temporarily stored images

	:param :
	:returns: No return
	"""
	for addr in addresses:
		src = addr[0] 
		des = addr[1] 
		Picture.objects.filter(file=src).update(file=des)

def process_files(files, uid, device_type, device): 
	""" This function processes all uploaded files

	:param 	capture_time: capture time of this file, only available for image files 
	:type 	capture_time: datetime.datetime 

	:return: None
	"""
	global sensor_file_path
	global is_finished
	global album_date

	for afile in files:
		process_file(afile, uid, device_type, device)
	# after save all files, update the end time of the last album

	date_info 	= update_last_album()

	if date_info is None:
		album_date      = datetime.now()
		date_info   = [album_date.year, album_date.month, album_date.day, album_date.hour, album_date.minute, album_date.second]

	# start a new thread to resize images to get thumbnails
	# one upload is finished
	# start to resize files and analyze 
	if is_finished:
		# analyze sensor file to get both date, time and sensor information
		# get a json format of information about the sensor here
		# uid here is for saving temporary data
		resize_files_thread(sensor_file_path,date_info,uid)


def update_last_album():
	""" This function processes every posted file according to their format

	:param 	capture_time: capture time of this file, only available for image files 
	:type 	capture_time: datetime.datetime 

	:return: None
	"""
	global album_date
	global is_finished
	global sensor_file_path
	global cur_album 

	if cur_album is not None:
		print cur_album.id
		print "album_end_time"
		print album_end_time
		#log = 1/None
		db_fileuploader_update_album_time(cur_album, album_start_time, album_end_time)
	if album_date is None:
		return None
	else:
		album_date 	= cur_album.capture_date
		date_info 	= [album_date.year, album_date.month, album_date.day, 0,0,0]
		return date_info


def process_file(afile, uid, device_type, device):
	""" This function processes every posted file according to their format
		image file will be stored in image table
		sensor file will be stored in sensor table

	TODO: Need to consider when sensor file is the first file to upload, then capture_at is None

	:param 	date_info: date information concludes year, month, day, hour, minute and second
	:type 	date_info: list
	:param 	afile: file that is posted 
	:type 	afile: InMemoryUploadedFile 
	:param 	uid: user id 
	:type 	uid: long 
	:param 	album_id: album id 
	:type 	album_id: long 
	:param 	capture_time: capture time of this file, only available for image files 
	:type 	capture_time: datetime.datetime 
	"""
	global image_ids 
	global sensor_file_path 
	global album_date 
	global temp_files

	print "=========process_autographer_file========="
	file_saved_path = ''
	filename 		= afile.name
	print filename
	filename 	= filename.lower()
	if '.txt' in filename:
		# Sensor file
		print "=========txt file========="
		temp_file = {"afile":afile,"uid":uid,"device_type":device_type,"device":device}
		temp_files.append(temp_file)
		#save_sensor_file(afile, uid, date_info)
	elif '.csv' in filename:
		print "=========csv file========="
		save_sensor_file(afile, uid, date_info)
	elif '.dat' in filename:
		# here all files are stored in a temp folder at first until there is a image.
		print "=========dat file========="
		#save_dat_file(afile, uid, date_info)
	elif '.jpg' in filename:
		print "=========jpg========="
		try:
			date_info 	= autographer_get_file_create_time(afile.name, device_type)
			#print date_info
			#log = 1/None
			save_image(afile, uid, date_info, device, device_type)
		#return image_path	
		except IntegrityError:
			print "same image, not saved"
			# insert into interaction log

def save_dat_file(afile, uid, date_info):
	"""This function saves dat file in a temparary folder

	:param 	afile: an file id 
	:type 	afile: File 
	:param 	uid: user id 
	:type 	uid: long 
	:param 	date_info: date information of the current image
	:type 	date_info: list of numbers

	:returns: None
	"""
	today_date = str(dt.now().date())
	#file_url = "temp/user_{id}/{td}_{file}".format(id=uid,td=today_date,file=afile.name)
	file_url = "temp/user_{id}/{file}".format(id=uid,file=afile.name)
	with open(file_url, 'wb+') as destination:
		# chuncks ensure that big files won't take too much of space
		for chunk in f.chunks():
			destination.write(chunk)
		destination.close()
	
def save_sensor_json_file_bk(data, uid, date):
	"""This function saves one day's sensor data into a json file stored in sensorjson folder/userid

	:param 	afile: an file id 
	:type 	afile: File 
	:param 	uid: user id 
	:type 	uid: long 
	:param 	date_info: date information of the current image
	:type 	date_info: list of numbers

	:returns: sensor file saved path
	"""
	url = "sensorjson/user_{id}/{file}".format(id=uid,file='sensorjson_'+str(date)+'.json')
	file_object = open(url, 'w')
	json.dump(data, file_object)

	# update album with adding json file addresses
	print "update album with sensor json file addresses"

def save_sensor_file(afile, uid, date_info):
	"""This function saves sensor files according to device type
	if Sensecam sensor file, save in a temparary folder with current date
	if Autographer sensor file, save in their date specific folder

	:param 	afile: an file id 
	:type 	afile: File 
	:param 	uid: user id 
	:type 	uid: long 
	:param 	date_info: date information of the current image
	:type 	date_info: list of numbers

	:returns: sensor file saved path
	"""
	global flag_temp
	global album_date 
	global sensor_file_path 

	if flag_temp:
		# this means it is needed to analyze the csv file to get file dates
		# store in a temperory folder first
		album_date 	= dt.now().date()
		new_file 	= SensorFile(file = afile, user=User(id=uid),capture_at=album_date)
		new_file.save()
		sensor_file_path 	= new_file.file.name
		#sensecam_sensor_get_time(sensor_file_path, uid)
		#print type(new_file.file)

		# get the date of the actual capture time
		#print ""
	else:
		# this is to process sensor file of autographer etc that does not need any temporary processing
		new_file 			= SensorFile(file = afile, user=User(id=uid),capture_at=album_date)
		new_file.save()
		sensor_file_path 	= new_file.file.name
		#print type(new_file.file)
	print sensor_file_path

def save_image(afile, uid, date_info, device, device_type):
	"""This function saves one image into database and cloud folder

	:param 	afile: an file id 
	:type 	afile: File 
	:param 	uid: user id 
	:type 	uid: long 
	:param 	date_info: date information of the current image
	:type 	date_info: list of numbers
	:param 	device: 
	:type 	device: 
	:param 	flag_temp: 
	:type 	flag_temp: 

	:returns: None
	"""
	global image_ids 
	global flag_temp
	global folders_to_resize
	global days_count
	global temp_album_id

	date_time = datetime(year=date_info[0],month=date_info[1],day=date_info[2], hour=date_info[3], minute=date_info[4], second=date_info[5]) 
	#print "_______________save_image_________________"
	#print "date_info"
	#print date_info
	#print "date_time"
	#print date_time
	#dont check for album until all images are stored,
	#initial album = None 
	album	= check_for_album(date_time,None,uid,device)
	if flag_temp:
		temp_album_id		= album.id
	#if flag_temp:
	#print "save in temporary folder"
	capture_time= date_time
	#new_file = Picture(file = afile, user=User(id=uid), year=date_info[0], month=date_info[1], \
	#	day=date_info[2], album=album, capture_at=capture_time)
	if device_type is DEVICE_TYPE_AUTOGRAPHER:
		album	= check_for_album(date_time,None,uid,device)
		new_file = Picture(file = afile, user=User(id=uid), year=date_info[0], month=date_info[1], \
			day=date_info[2], album=album, capture_at=capture_time)
	elif device_type is DEVICE_TYPE_AUTOGRAPHER_U:
		album	= check_for_album(date_time,None,uid,device)
		new_file = Picture(file = afile, user=User(id=uid), year=date_info[0], month=date_info[1], \
			day=date_info[2], album=album, capture_at=capture_time)
	elif device_type is DEVICE_TYPE_SENSECAM:
		new_file = Picture(file = afile, user=User(id=uid), year=date_info[0], month=date_info[1], \
			day=date_info[2], album=album, capture_at=capture_time)
		#new_file = Picture(file = afile, album=None, user=User(id=uid))
	new_file.save()
	img_id				= new_file.id
	#print "img_id"
	#print img_id
	# each image_path is a relavant path to the project media folder
	filename = afile.name
	#print filename
	image_ids[filename] = img_id
	"""
	else:
		capture_time= datetime(date_info[0],date_info[1],date_info[2],\
			date_info[3],date_info[4],date_info[5])
		new_file = Picture(file = afile, user=User(id=uid), year=date_info[0], month=date_info[1], \
			day=date_info[2], album=album, capture_at=capture_time)
		new_file.save()
		img_id				= new_file.id
		print "img_id"
		print img_id
		# each image_path is a relavant path to the project media folder
		filename = afile.name
		print filename
		image_ids[filename] = img_id
	"""

def check_for_album(start_time, end_time, uid, device):
	""" This function checks whether it is a new album. 
		First, it checks whether there is an album with the same date and same user in the database
		If it should be a new album, store current album and initiate a new album, album start time initiate 
		If it is still in the same album, current time is the album end time
		to-do: check for the same album

	:param 	date_info: date information concludes year, month, day, hour, minute and second, should be the start time
	:type 	date_info: list
	:param 	uid: user id 
	:type 	uid: long 
	:param 	album_date: album date
	:type 	album_date: datetime.date 

	:return: album id
	"""
	# global variables
	global cur_album
	global album_date 
	global album_start_time
	global album_end_time

	# each image has to belong to an album
	#cur_date 	= date(date_info[0],date_info[1],date_info[2])
	#cur_time	= datetime(year=date_info[0],month=date_info[1],day=date_info[2], hour=date_info[3], minute=date_info[4], second=date_info[5]) 
	time_format = '%Y-%m-%d %H:%M:%S'
	if isinstance(start_time, basestring):
		album_start_time = datetime.strptime(start_time, time_format)
		album_end_time = datetime.strptime(end_time, time_format)
		cur_date 	= album_end_time.date()
	else:
		album_start_time = start_time
		cur_date 	= album_start_time.date()

	#cur_date 	= album_end_time.date()
	cur_time	= album_start_time

	# if the album exists in the database, directly return the album id
	# find the album exists in the database, update either start_at or end_at
	cur_album = db_fileuploader_get_album(uid, cur_date)
	if cur_album is not None:
		#print cur_album
		#print album_start_time
		#print album_end_time 
		#print "_______________________________________"
		#print album_start_time
		#print album_end_time
		#print "_______________________________________"
		db_fileuploader_update_album_time(cur_album, album_start_time, album_end_time) 
		album_start_time 	= cur_album.start_at
		album_end_time 		= cur_album.end_at
		update_album_start_end_time(cur_time)
		return cur_album

	# if there is no such album in the database
	# create a new album in the database
	# print cur_album
	# print album_date
	# print album_start_time
	# print album_end_time
	# start a new album
	if end_time is not None:
		album_end_time = end_time
	else:
		album_end_time = cur_time
	# album_start_time 	= cur_time
	album_date 			= cur_date 
	cur_album 			= Album(user=User(id=uid), device=device, capture_date=album_date, \
		start_at=album_start_time, end_at=album_end_time)
	cur_album.save()
	return cur_album

	"""
	# same album, keep parsing
	if cur_date == album_date:
		print "same date"
		# update the album end time 
		album_end_time = cur_time 
	# a new date, a new album and save
	else:
		print "not same date"
		# album_duration	= (cur_time-album_start_time).seconds
		if album_date is not None: # a new sensor file, dont save
			# update previous album end time
			db_fileuploader_update_album_endtime(cur_album, album_end_time) 
		# album_end_time  	= album_start_time = cur_time
		# start a new album
		album_end_time  	= album_start_time = cur_time
		# album_start_time 	= cur_time
		album_date 			= cur_date 
		cur_album 			= Album(user=User(id=uid), device=device, capture_date=album_date, \
			start_at=album_start_time, end_at=album_end_time)
		cur_album.save()
	"""

	return cur_album 

def update_album_start_end_time(cur_time):
	""" This function checks whether it is a new album. 

	:param 	cur_time: date information concludes year, month, day, hour, minute and second
	:type 	cur_time: list

	:return: album id
	"""
	# global variables
	global album_start_time
	global album_end_time
	#cur_time = cur_time.replace(tzinfo=TIME_ZONE)
	cur_time = get_datetime_timezone(cur_time)

	if album_end_time is None:
		album_end_time = cur_time
	elif album_end_time < cur_time:
		album_end_time = cur_time
	elif album_start_time > cur_time:
		album_start_time = cur_time
	return
