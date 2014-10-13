"""File relevant operations class
   This class includes all file relevant operations 

.. module:: common 
   :platform: Ubuntu Unix
   :synopsis: A module for all type file relevant process 

.. moduleauthor:: Lijuan Marissa Zhou <marissa.zhou.cn@gmail.com>

"""
import sys
sys.path.append(sys.path[0]+'/lib/common/db')

import json
import os
import math
import scipy
import shutil
from threading import Thread
from time import sleep
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from scipy.stats import norm,lognorm
#from fileuploaderHelper import *

from memlog_settings import *

'''
 	constants for distritubion types	
'''
DIST_TYPE_NORMAL 	= 0

def print_test(albums, date_info, uid):
	print date_info

def files_move_files(albums, date_info, uid):
	"""This function move files from one place to another place 
	
	:param albums: directory address string 
	:type albums: string 
	:param extention: file type that is wanted to be retrieved 
	:type extention: string 
	:returns: file address list 
	"""
	addresses = [] # [[0,1]]
	dates = albums.keys()
	for cur_date in dates:
		for sensor_record in albums[cur_date]:
			if sensor_record['cam'] is not None: # there is a photo for this record
				url1 = "img/user_{id}/{y}/{m}/{d}/{file}".format(id=uid,y=date_info[0],m=date_info[1],d=date_info[2],file=sensor_record['cam'])
				url2 = "img/user_{id}/{y}/{m}/{d}/{file}".format(id=uid,y=cur_date.year,m=cur_date.month,d=cur_date.day,file=sensor_record['cam'])
				addresses.append([url1,url2])
        		src = settings.MEDIA_ROOT + url1
        		dst = settings.MEDIA_ROOT + url2
        		shutil.move(src, dst)
	# build one connection and update image paths in database
	update_image_file_addresses(addresses)

def retrievel_files(dir_path, extention):
	'''This function retrieves all extention files in a given folder 
	
	:param dir: directory address string 
	:type dir: string 
	:param extention: file type that is wanted to be retrieved 
	:type extention: string 
	:returns: file address list 
	'''
	try:
		dir = File(dir_path)
		if not os.path.isdir(dir_path):
			return []
		else:
			files 		= [] # files with extension
			all_files 	= os.listdir(dir_path) #
			for file in all_files:
				if os.path.isdir(file):
					# do something
					print ""
				else:
					file_name, file_ext= os.path.splitext(file)
					if is_equal_case_insensitive(file_ext, extension): 
						files.append(file)
			for file in os.listdir(dir_path):
				print ""
	except ValueError:
		# write into log DB
		print "Oops!  That was no valid number.  Try again..."
	return files 

def retrieve_all_files_in_dir(file_path, extension, files):
	'''This function recursively get all files of the type in the directory
	
	:param file_path: path of the directory 
	:type file_path: string 
	:param extension: extension 
	:type extension: string 
	:param files: to store all files in the list 
	:type files: list 
	:returns: file address list 
	'''
	try:
		dir = File(dir_path)
		if not os.path.isdir(dir_path):
			return []
		else:
			files 		= [] # files with extension
			all_files 	= os.listdir(dir_path) #
			for file in all_files:
				if os.path.isdir(file):
					print ""
					# do something
					retrieve_all_files_in_dir(file, extension, files)
				else:
					file_name, file_ext= os.path.splitext(file)
					if is_equal_case_insensitive(file_ext, extension): 
						files.append(file)
			for file in os.listdir(dir_path):
					print ""
	except ValueError:
		# write into log DB
		print "Oops!  That was no valid number.  Try again..."
	return files 

def is_equal_case_insensitive(str1, str2):
	'''This function check whether two string equal case insensitively 
	
	:param str1: string 1 
	:type str1: string 
	:param str2: string 2 
	:type str2: string 
	:returns: file address list 
	'''
	try:
		if str1.lower() == str2.lower():
			return True
		else:
			return False
	except ValueError:
		# write into log DB
		print "Oops!  That was no valid number.  Try again..."

def walk_sensor_file(afile, uid, device_type):
    """ This function walks through sensor file and store all sensor information into database 

    :param  afile: file that is posted 
    :type   afile: InMemoryUploadedFile 
    :param  uid: user id 
    :type   uid: long 
    :param  device_type: device type: sensecam or autographer or android phone
    :type   device_type: int 
    """
    cur_date    = date(date_info[0],date_info[1],date_info[2])

def save_sensor_json_file(data, uid, capture_date):
	year 	= str(capture_date.year)
	month 	= str(capture_date.month)
	date 	= str(capture_date)
	user 	= "user_"+str(uid)
	file_path = os.path.join(SENSOR_JSON_ROOT,user,year,month,date+".json")
	dir_path = os.path.dirname(file_path)
	#print "save_sensor_json_file(data, uid, capture_date) in files"
	#print file_path
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)

	write_json_object(data, file_path)

def write_json_object(data, file_path):
    """ This function writes json data into a local file

    :param  file_path: file that is posted 
    :type   file_path: InMemoryUploadedFile 
    """
    with open(file_path, 'w') as outfile:
    	json.dump(data, outfile)

class MediaFileSystemStorage(FileSystemStorage):
	def get_available_name(self, name):
		"""Returns a filename that's free on the target storage system, and
		available for new content to be written to.

		Found at http://djangosnippets.org/snippets/976/
		Refer to: http://stackoverflow.com/questions/15885201/django-uploads-discard-uploaded-duplicates-use-existing-file-md5-based-check

		This file storage solves overwrite on upload problem. Another
		proposed solution was to override the save method on the model
		like so (from https://code.djangoproject.com/ticket/11663):

		def save(self, *args, **kwargs):
			try:
			this = MyModelName.objects.get(id=self.id)
			if this.MyImageFieldName != self.MyImageFieldName:
			this.MyImageFieldName.delete()
			except: pass
				super(MyModelName, self).save(*args, **kwargs)
		"""
		return name

	def _save(self, name, content):
		if self.exists(name):
			# if the file exists, do not call the superclasses _save method
			return name
			# if the file is new, DO call it
		return super(MediaFileSystemStorage, self)._save(name, content)


class OverwriteStorage(FileSystemStorage):
	def _save(self, name, content):
		if self.exists(name):
			self.delete(name)
		return super(OverwriteStorage, self)._save(name, content)

	def get_available_name(self, name):
		return name


def move_files_thread_bk(albums, date_info, uid):
	"""This function move files from one place to another place 
	
	:param dir: directory address string 
	:type dir: string 
	:param extention: file type that is wanted to be retrieved 
	:type extention: string 
	:returns: file address list 
	"""
	thread = Thread(target = move_files, args = (albums, date_info, uid))
	thread.start()
	# Wait for all of them to finish
	thread.join()

def sensecam_sensor_get_time(file_path, uid):
	""" This function writes json data into a local file
	:param  file_path: file that is posted 
	:type   file_path: InMemoryUploadedFile 
	"""
	capture_date = None
	with open(file_path, 'rb') as csvfile:
		filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
		time_format = '%Y-%m-%d %H:%M:%S'
		for row in filereader:
			dt = datetime.strptime(row[1], time_format)
			capture_date = dt.date()
	return capture_date
