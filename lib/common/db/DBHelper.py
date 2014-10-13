#!/usr/bin/env python
"""overall database manipulation class
.. module:: DBHelper
   :platform: Ubuntu Unix
   :synopsis: A module for general database connection
   
.. moduleauthor:: Lijuan Marissa Zhou <marissa.zhou.cn@gmail.com>
.. copyright:: copyright reserved 


Image file names:
SenseCam 	- 00031075.JPG
Vicon		- 00011328.JPG -> 0_0_date_time.j
Autographer - B00000781_21I5I2_20140303_1200294.JPG

"""
import _mysql
import MySQLdb as mdb
import unicodedata
from timeutils import *
from datetime import datetime as dt
from threading import Thread
from time import sleep
from django.db import IntegrityError
from dateutil.tz import tzlocal
from xml.dom import minidom

#from fileuploader.models import *

class DBHelper:

	# database connection
	con = None 

	@staticmethod
	def initialize():
		"""This function initializes an DBHelper instance
		:param :
		:returns:
		"""
		DBHelper.con = mdb.connect('localhost', 'root', 'sensepass', 'sensecambrowser')

	@staticmethod
	def update_picture_record(addresses, album_ids):
		"""	This function updates all image addresses in the database image table
			Initialise MYSQL connection
		:param :
		:returns: No return
		"""
		import time    
		time.strftime('%Y-%m-%d %H:%M:%S')
		con = mdb.connect('localhost', 'root', 'sensepass', 'sensecambrowser')
		print album_ids
		for row in addresses:
			with con:
				capture_time   = row[2]
				infos = row[1].split("/")
				#date_string = infos[2]+"-"+infos[3]+"-"+infos[4]
				date_string =  str(capture_time.date())
				#print date_string
				aid = album_ids[date_string]# album id
				cur = con.cursor()
				para_1 = "'"+	row[1]+"'"
				para_2 = aid
				para_3 = infos[2]
				para_4 = infos[3]
				para_5 = infos[4]
				para_6 = "'"+	row[0]+"'"
				capture_time   = row[2]
				query = "UPDATE fileuploader_picture SET file=%s,album_id=%s,year=%s,month=%s,day=%s,capture_at=CAST('%s' AS DATETIME) WHERE file=%s" % (para_1,para_2,para_3,para_4,para_5,capture_time,para_6,)
				print query
				#print query
				cur.execute(query)

	@staticmethod
	def update_sensor_file(src, dst):
		"""	This function updates all sensor_file_records
			Initialise MYSQL connection

		:param :
		:returns: No return
		"""
		con = mdb.connect('localhost', 'root', 'sensepass', 'sensecambrowser')
		with con:
			src = "'"+	src+"'"
			dst = "'"+	dst+"'"
			query = "UPDATE fileuploader_sensorfile SET file=%s WHERE file=%s" % (src,dst)
			cur = con.cursor()
			cur.execute(query)


	@staticmethod
	def remove_empty_albums(aid):
		"""	This function keeps album table clean without any empty albums
		Empty albums are albums that has no picture associated with that album
		This is necessary when uploading SenseCam images which are uploaded in a temporary album at the beginning and a temporary album is created for this purposes

		:param aid: album id
		:type aid: big integar
		:returns: No return
		"""
		print "aid"
		print aid
		if aid is None:
			return
		con = mdb.connect('localhost', 'root', 'sensepass', 'sensecambrowser')
		with con:
			query = "SELECT count(*) from fileuploader_picture WHERE album_id=%s" % (aid)
			cur = con.cursor()
			cur.execute(query)
			data = cur.fetchall()
			# there is no picture in this album
			print "len(data)"
			print len(data)
			if len(data) == 0:
				query = "DELETE from fileuploader_album WHERE id=%s" % (aid)
				print query
				cur = con.cursor()
				cur.execute(query)

	@staticmethod
	def get_uid(username):
		"""	This function retrieves user id according to username

		:param aid: album id
		:type aid: big integar
		:returns: No return
		"""
		if username is None:
			return
		con = mdb.connect('localhost', 'root', 'sensepass', 'sensecambrowser')
		with con:
			query = "SELECT id from auth_user WHERE username=%s" % (username)
			cur = con.cursor()
			cur.execute(query)
			data = cur.fetchall()
			print "len(data)"
			print data
			if len(data) > 0:
				return data[0]
			return None

	@staticmethod
	def get_sensor_type_id(abbreviation):
		"""	This function retrieves sensor type id according to abbreviation

		:param abbreviation: sensor type abbreviation
		:type abbreviation: string
		:returns: No return
		"""
		if abbreviation is None:
			return
		con = mdb.connect('localhost', 'root', 'sensepass', 'sensecambrowser')
		with con:
			query = "SELECT id from fileuploader_sensortype WHERE abbreviation=%s" % (abbreviation)
			cur = con.cursor()
			cur.execute(query)
			data = cur.fetchall()
			print "len(data)"
			print data
			if len(data) > 0:
				return data[0]
			return None

	@staticmethod
	def get_picture_id(path):
		"""	This function retrieves user id according to username

		:param aid: album id
		:type aid: big integar
		:returns: No return
		"""
		if path is None:
			return
		con = mdb.connect('localhost', 'root', 'sensepass', 'sensecambrowser')
		with con:
			query = "SELECT id from fileuploader_picture WHERE file=%s" % (path)
			cur = con.cursor()
			cur.execute(query)
			data = cur.fetchall()
			print "len(data)"
			print data
			if len(data) > 0:
				return data[0]
			return None

	@staticmethod
	def get_concept_id(concept):
		"""	This function retrieves user id according to username

		:param aid: album id
		:type aid: big integar
		:returns: No return
		"""
		if path is None:
			return
		con = mdb.connect('localhost', 'root', 'sensepass', 'sensecambrowser')
		with con:
			query = "SELECT id from annotater_annotationterm WHERE concept=%s" % (concept)
			cur = con.cursor()
			cur.execute(query)
			data = cur.fetchall()
			print "len(data)"
			print data
			if len(data) > 0:
				return data[0]
			return None

	@staticmethod
	def insert_annotationactions(annotations):
		"""	This function add all annotation records into database through one database connection

		:param annotations: annotations list extracted from exported annotation file from the old sensecambrowser system
		:type annotations: list of 3 dimensional list
		:returns: No return
		"""
		if annotations is None:
			return
		con = mdb.connect('localhost', 'root', 'sensepass', 'sensecambrowser')
		with con:
			for annotation in annotations:
				username = annotation[0]
				path = annotation[1]
				concept = annotation[2]
				uid = DBHelper.get_user_id(username)
				iid = DBHelper.get_user_id(path)
				cid = DBHelper.get_user_id(concept)
				query = "insert into annotater_annotationaction(annotator_id,image_id,concept_id) values(%s,%s,%s)" % (uid,iid,cid)
				cur = con.cursor()
				cur.execute(query)

	@staticmethod
	def insert_sensors(sensors):
		"""	This function adds all sensor records into the new database through one database connection

		:param sensors: sensors list extracted from exported sensor file from the old sensecambrowser system
		:type sensors: list of sensor list
		:returns: No return
		"""
		if sensors is None:
			return
		con = mdb.connect('localhost', 'root', 'sensepass', 'sensecambrowser')
		with con:
			for sensor in sensors:
				"""
				username = annotation[0]
				path = annotation[1]
				concept = annotation[2]
				uid = DBHelper.get_user_id(username)
				iid = DBHelper.get_user_id(path)
				cid = DBHelper.get_user_id(concept)
				query = "insert into annotater_annotationaction(annotator_id,image_id,concept_id) values(%s,%s,%s)" % (uid,iid,cid)
				cur = con.cursor()
				cur.execute(query)
				"""
