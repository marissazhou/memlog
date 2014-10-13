""" 
   This class images  
.. module:: common 
   :platform: Ubuntu Unix
   :synopsis: A module for all type of mathematical operation needed for Prime model

.. moduleauthor:: Lijuan Marissa Zhou <marissa.zhou.cn@gmail.com>

"""
import scipy
from datetime import datetime, date, time
#import Image
import os
from os import walk
#from PIL import Image, ImageOps
import Image
from memlog_settings import *
from django.conf import settings

"""
constants for 
"""

def get_key_frame_for_event(images):
	"""	This function returns keyframe for events in lifelogging system. 
	
	The algorithms to get key frame could be:
	algorithm 1:
	
	:param images: images list 
	:type images: list 
	:returns:  the absolute address of key frame image
	"""
	return images[0]

def resize_image_list(image_list):
	"""	This function iterates all images in image_list
		could be used in a thread
	
	:param 	folder: images folder to resize 
	:type 	folder: string 
	:returns:
	"""
	#print "----------image_list to resize 1-----------------"
	#print image_list
	#print len(image_list)
	if image_list == None:
		return
	elif len(image_list) < 1:
		return 
	#print image_list

	for image_filename in image_list:
		# print image_filename
		#log = 1/None
		image_filename = os.path.join(settings.MEDIA_ROOT,image_filename['file'])
		#print "image_filename = image_filename['file']"
		#print "resize:----------------image_filename-----------------"
		file_name = os.path.basename(image_filename)
		#print file_name 
		dir_path = os.path.dirname(image_filename)
		resize_image(dir_path, file_name)
	return 

def resize_image_folder(folders):
	"""	This function iterates all folders in array folders
		could be used in a thread
	
	:param 	folder: images folder to resize 
	:type 	folder: string 
	:returns:
	"""
	#print folders
	if folders == None:
		return
	elif len(folders) < 1:
		return
	for (dir_path, dirnames, filenames) in walk(folders):
		# both autographer and sensecam images are JPG images
		if "thumb" in dir_path:
			continue	
		for image_filename in filenames:
			resize_image(dir_path, image_filename)
	return 

def resize_image(dir_path, image_filename):
	"""This function resizes one image 
	http://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
	
	:param image_filename: 
	:type image_filename: string 
	:returns:
	"""
	size = (256, 192)
	if '.JPG' in image_filename:
		infile = dir_path+"/"+image_filename
		outfile = dir_path+"/thumbs/"+image_filename
		out_dir = dir_path+"/thumbs/"
		if not os.path.exists(out_dir):
			os.makedirs(out_dir)
		#print "------------------infile and outfile-----------------"
		#print dir_path 
		#print infile
		#print outfile
		if infile != outfile:
			try:
				#print "infile != outfile"
				im = Image.open(infile)
				im.thumbnail(size, Image.ANTIALIAS)
				im.save(outfile, "JPEG")
				#thumb = ImageOps.fit(im, size, Image.ANTIALIAS)
			except IOError:
				print "cannot create thumbnail for '%s'" % infile
	return 
