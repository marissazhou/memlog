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
import json
import csv
import scipy
from threading import Thread
from db.DBHelper import DBHelper
from datetime import datetime, date, time
from django.conf import settings
from memlog_settings import *
from files import *
from timeutils import *
from stringutils import *
from django.db import IntegrityError

'''
	MODELS
'''
from fileuploader.models import *

'''
 	CONSTRAINTS	
'''
sensor_list = []
sensor_type_dict = None

def move_files(albums, album_ids, date_info, uid):
    """This function move files from one place to another place 
    
    :param albums: directory address string 
    :type albums: string 
    :param extention: file type that is wanted to be retrieved 
    :type extention: string 
    :returns: file address list 
    """
    #print "&&&&&&&&&&&&&& move_files &&&&&&&&&&&&&&&&&&" 
    addresses = [] # [[0,1]]
    dates = albums.keys()
    #print "dates" 
    #print dates 
    time_format = '%Y-%m-%d %H:%M:%S'
    capture_time = None
    for cur_date in dates:
        for sensor_record in albums[cur_date]:
            if 'CAM' in sensor_record: # there is a photo for this record

                capture_time = sensor_record['time']
                # capture_time = datetime.strptime(capture_time, time_format)
                capture_time = string_2_datetime(capture_time)

                #dst_date_info = cur_date.split("-")
                #year = dst_date_info[0]
                #month = dst_date_info[1]
                #day = dst_date_info[2]
                year = capture_time.year
                month = capture_time.month
                day = capture_time.day
                url1 = "img/user_{id}/{y}/{m}/{d}/{file}".format(id=uid,y=date_info[0],m=date_info[1],d=date_info[2],file=sensor_record['CAM'])
                url2 = "img/user_{id}/{y}/{m}/{d}/{file}".format(id=uid,y=year,m=month,d=day,file=sensor_record['CAM'])
                #addresses.append([url1,url2])
                src = settings.MEDIA_ROOT + url1
                dst = settings.MEDIA_ROOT + url2
                #src = url1
                #dst = url2
                dst_dir = os.path.dirname(dst)
                if not os.path.exists(dst_dir):
					os.makedirs(dst_dir)
                if os.path.isfile(src):
					#print src
					#print dst
					"""
					print "----------------------------"
					print "Move Files"
					print src
					print dst
					print "----------------------------"
					"""
					addresses.append([url1,url2,capture_time])
					shutil.move(src, dst)
    #print "**************** addresses *************" 
    #print addresses
    # build one connection and update image paths in database
    DBHelper.update_picture_record(addresses, album_ids)


def get_minutes(time):
	'''This function returns minute of events 
	
	:param time: time 
	:type time: string 
	:returns: normal distribution 
	'''
	arr = time.split(" ")[1].split(":")
	if arr[1] < "12":
		return arr[0]+":"+arr[1]+" am"
	else:
		return arr[0]+":"+arr[1]+" pm"


def autographer_string_to_datetime(dt):
	'''This function returns the datetime format of dt string for autographer data format 
       Note 1: strptime() is independent of any platform and thus does not necessarily support all directives available that are not documented as supported.
	
	:param dt: date time 
	:type dt: string 
	:returns: datetime.datetime of dt string
	'''
   
	time_format = '%Y-%m-%dT%H:%M:%S'
	timezone_sep = '+'
	dts = dt.split(timezone_sep)
	# dt_strptime = datetime.strptime(dts[0], time_format)
	dt_strptime = string_2_datetime(dts[0])
	#dt_obj		= datetime(dt_strptime)
	return dt_strptime


def is_same_date(date_1, date_2):
	'''This function returns minute of events 
       Note 1: strptime() is independent of any platform and thus does not necessarily support all directives available that are not documented as supported.
	
	:param dt: date time 
	:type dt: string 
	:returns: datetime.datetime of dt string
	'''
	
	if (not isinstance(date_1, date)) or (not isinstance(date_2, date)):
		# raise an not date formate exception
		return False
	if date_1 == date_2:
		return True
	else:
		return False

def get_pic_address(pic_name, device_type):
	'''This function returns picture address according to picture address 
	
	:param pic_name: picture name, same as in sensor file 
	:type pic_name: string 
	:returns: picture full address 
	'''
	if device_type is DEVICE_TYPE_AUTOGRAPHER:
		# raise an not date formate exception
		pic_names = pic_name.split("_")
		pic_address = MEDIA_ROOT + pic_names[2][:2] +"\\"+ pic_names[2][2:4] +"\\" + pic_names[2][4:] +"\\" + pic_name 
		return pic_address 

	elif device_type is DEVICE_TYPE_SENSECAM:
		return "" 
	else:
		return "" 

def write_log_user_interaction(uid, log_type, message):
	'''This function write user interaction logs into either json file or database, json is a preference cos it saves spaces in database 
	
	:param uid: user id 
	:type uid: int 
	:param log_type: log type for different types of logs 
	:type log_type: int 
	:param message: message that is to be written 
	:type message: string 
	:returns: picture full address 
	'''
	if log_type is LOG_TYPE_USER_OPERATION:
		print "Write Log User Operation"
		return
	elif log_type is LOG_TYPE_USER_ANNOTATION:
		print "Write Log User Annotation"
		return
	elif log_type is LOG_TYPE_USER_WARNING:
		print "Write Log User Warning"
		return
	else:
		return

def autographer_get_file_create_time(filename, device_type):
	"""This function get file creation time according to filename like 'B00003827_21I5I2_20140211_0827134.JPG' in Autographer 
	TO DO: add other devices filename split module
	
	:param filename: file name, like autographer image name 
	:type filename: string
	:returns: [year, month, date] 
	"""
	#print filename
	#print "device_type"
	#print device_type
	
	if device_type is DEVICE_TYPE_AUTOGRAPHER:
		strs = filename.split('_')
		# year, month, date, hour, min, second
		year 	= int(strs[2][:4])
		month	= int(strs[2][4:6])
		day		= int(strs[2][6:])
		hour	= int(strs[3][:2])
		minute	= int(strs[3][2:4])
		second	= int(strs[3][4:6])
		date_info = [year, month, day, hour, minute, second]
		return date_info 
	elif device_type is DEVICE_TYPE_AUTOGRAPHER_U:
		strs = filename.split('_')
		# year, month, date, hour, min, second
		year 	= int(strs[2][:4])
		month	= int(strs[2][4:6])
		day		= int(strs[2][6:])
		hour	= int(strs[3][:2])
		minute	= int(strs[3][2:4])
		second	= int(strs[3][4:6])
		date_info = [year, month, day, hour, minute, second]
		return date_info 
	elif device_type is DEVICE_TYPE_SENSECAM:
		strs = filename.split('_')
		return []
	elif device_type is DEVICE_TYPE_NARRATIVE:
		return []
	else:
		return []

def get_time_diff_h_m_s(dt1, dt2):
	"""This function get returns the difference between two times in the format of (hours, mins, secs)
	
	:param 	dt1: datetime one 
	:type 	dt1: datetime 
	:param 	dt2: datetime two
	:type 	dt2: datetime 
	:returns: (hours, mins, secs)
	"""
	if dt2 > dt1:
		diff = dt2 - dt1
		(min, secs) = divmod(diff.days * 86400 + diff.seconds, 60)
		(hours, mins) = divmod(min, 60)
		return (hours,mins,secs)
	else:
		return (0,0,0)

def get_date_dash_d_m_y(datetime_date):
	"""This function returns the datetime.date object to "d/m/y" format 
	
	:param 	datetime_date: datetime date object to be converted 
	:type 	datetime_date: datetime.date 
	:returns: (hours, mins, secs)
	"""
	new_date = get_string_for_time(datetime_date.day)+'/' \
			+ get_string_for_time(datetime_date.month)+'/' \
			+ get_string_for_time(datetime_date.year) 
	return new_date

def get_string_for_time(inte):
	if inte < 10:
		return '0'+str(inte)
	else:
		return str(inte)
	
def get_sensor_type_dict():
	""" This function fetches all sensor types in the database for global usage
	The fuction allows to fetch SensorType objects directly from memory instead of creating a new object each time
	"""
	global sensor_type_dict
	sensor_type_dict = {} 

	instances = SensorType.objects.all().values("abbreviation")
	for instance in instances:
		abbr = instance["abbreviation"]
		#print abbr
		sensor_type = SensorType.objects.get(abbreviation=abbr)
		#print sensor_type
		sensor_type_dict[str(abbr)] = sensor_type

def sensecam_analyze_sensor(file_path, uid):
	"""This function analyze sensor folder for snesecam sensor file and return information including:
		1. date of capture, dateinfo 6 elements ();  a list to store this to create album [id | uid | start_at            | end_at              | capture_date | annotation | uploaded_at         | device_id]
		2. time of picutures
		3. save sensors in json format, a new thread to do this
			the format of json should be:
			[{"ACC":,"TMP":,"CLR":"PIR":"BAT":"MAG":,"CAM":},{}]
	
	:param 	file_path: file path 
	:type 	file_path: string
	:returns: albums = {"date":[{"image":,"pir":}]}
	"""
	global sensor_list
	global sensor_type_dict
	if sensor_type_dict == None:
		get_sensor_type_dict()
	sensor_list = [] # Sensor type list [Sensor(user=User(id=uid), sensor_type=sensor_type, capture_at=time, value=value),]
	albums = {} # store all sensor captures in a json format for later moving temporary data into their folders with date 
	# albums = {"date":[{"image":,"pir":}]}
	file_capture_date = None
	#print "-------------------------------"
	#print "file_path in sensecam_analyze_sensor"
	#print file_path
	#print "-------------------------------"
	count = 1
	is_head = True # head of file, discard
	prev_date = None
	json_file_path= file_path.replace("csv","json") # file path to write objects
	album = [] # list of captures of one day
	#album = [{"image":,"pir":}] # list of captures of one day
	file_capture_date = None
	with open(file_path, 'rb') as csvfile:
		filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
		one_capture = None 
		# move sensor file 
		row = filereader.next()
		file_capture_date = string_2_datetime(row[1]).date()
		# process sensor file content
		for row in filereader:
			label 		= row[0]
			#start of captures
			if label == 'ACC':
				if is_head is True:
					is_head = False
				# get time information
				#current_dt	= datetime.strptime(row[1], '%Y/%m/%d %H:%M:%S')
				current_dt = string_2_datetime(row[1])
				current_date= current_dt.date()
				if prev_date is None:
					prev_date = current_date
				# should be in the same album
				# 1. first save one_capture
				(time, label, value) = sensecam_analyze_sensor_row(uid, row, label)
				# 2. save previous one_capture 
				if one_capture is not None:
					album.append(one_capture) #one album has many one_captures
				one_capture = {} # initiate a new one_capture 
				one_capture['time'] = str(time)
				one_capture[label] = value

				if current_date == prev_date: 
					# same date
					if value is not None:
						one_capture[label] = value
				else:
					# different dates
					#print "----current_date and prev_date-------------"
					#print current_date
					#print prev_date
					#print "-------------------------------------------"
					if prev_date is not None:
						# save current album and initiate a new album
						albums[str(prev_date)] = album
						# save sensor json file for current date
						save_sensor_json_file(album, uid, prev_date)
					# initiate for the next album
					album = []
					prev_date = current_date
				# print label
				# start recording all captures
				# one day's data will be stored in json
				#start_new_capture(filereader, row, label, prev_date, captures, one_capture, uid)
			else:
				# either head or same capture
				if is_head is True:
					continue
				else:
					#is not head, need to add into current one_capture
					(time, label, value) = sensecam_analyze_sensor_row(uid, row, label)
					if value is not None:
						one_capture[label] = value
	#albums={"date":[{"image":,"pir":}]}
	# move sensor file 
	# sensor_file_path = move_sensecam_sensor_file(file_capture_date, file_path)
	#print albums.keys()
	utils_batch_insert_sensor_thread()

	albums[str(current_date)] = album
	return (albums,file_capture_date)  

def save_previous_album(date,album):
	print ""
	

def test_filereader(file_path):
	with open(file_path, 'rb') as csvfile:
		filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
		while True:
			row = filereader.next()
			print row
			if row == None:
				print "row == None"


def sensecam_analyze_sensor_row(uid, row, label):
	"""This function analyze one row of sensor file
			[{"ACC":,"TMP":,"CLR":"PIR":"BAT":"MAG":,"CAM":},{}]
	
	:param 	file_path: file path 
	:type 	file_path: string
	:returns: datetime.date
	"""
	global sensor_list
	global sensor_type_dict
	#print "~~~~in sensecam_analyze_sensor_row ~~~~"
	# time = datetime.strptime(row[1], '%Y/%m/%d %H:%M:%S')
	time = string_2_datetime(row[1])
	#print row
	if label == "ACC":
		#utils_insert_sensor(uid,"accx",row[2],time)
		sensor_1 = Sensor(user=User(id=uid), sensor_type=sensor_type_dict["accx"], capture_at=time, value=row[2])
		sensor_2 = Sensor(user=User(id=uid), sensor_type=sensor_type_dict["accy"], capture_at=time, value=row[3])
		sensor_3 = Sensor(user=User(id=uid), sensor_type=sensor_type_dict["accz"], capture_at=time, value=row[4])
		sensor_list.append(sensor_1) # Sensor type list [Sensor(user=User(id=uid), sensor_type=sensor_type, capture_at=time, value=value),]
		sensor_list.append(sensor_2) # Sensor type list [Sensor(user=User(id=uid), sensor_type=sensor_type, capture_at=time, value=value),]
		sensor_list.append(sensor_3) # Sensor type list [Sensor(user=User(id=uid), sensor_type=sensor_type, capture_at=time, value=value),]
		return (time, "ACC",{"accx":row[2],"accy":row[3],"accz":row[4]})
	elif label == "TMP":
		sensor_1 = Sensor(user=User(id=uid), sensor_type=sensor_type_dict["tmp"], capture_at=time, value=row[2])
		sensor_list.append(sensor_1) # Sensor type list [Sensor(user=User(id=uid), sensor_type=sensor_type, capture_at=time, value=value),]
		# utils_insert_sensor(uid,"tmp",row[2],time)
		return (time, "TMP",row[2])
	elif label == "CLR":
		sensor_1 = Sensor(user=User(id=uid), sensor_type=sensor_type_dict["clr"], capture_at=time, value=row[2])
		sensor_list.append(sensor_1) # Sensor type list [Sensor(user=User(id=uid), sensor_type=sensor_type, capture_at=time, value=value),]
		#utils_insert_sensor(uid,"clr",row[2],time)
		return (time, "CLR",row[2])
	elif label == "PIR":
		sensor_1 = Sensor(user=User(id=uid), sensor_type=sensor_type_dict["pir"], capture_at=time, value=row[2])
		sensor_list.append(sensor_1) # Sensor type list [Sensor(user=User(id=uid), sensor_type=sensor_type, capture_at=time, value=value),]
		#utils_insert_sensor(uid,"pir",row[2],time)
		return (time, "PIR",row[2])
	elif label == "BAT":
		sensor_1 = Sensor(user=User(id=uid), sensor_type=sensor_type_dict["bat"], capture_at=time, value=row[2])
		sensor_list.append(sensor_1) # Sensor type list [Sensor(user=User(id=uid), sensor_type=sensor_type, capture_at=time, value=value),]
		#utils_insert_sensor(uid,"bat",row[2],time)
		return (time, "BAT",row[2])
	elif label == "MAG":
		sensor_1 = Sensor(user=User(id=uid), sensor_type=sensor_type_dict["magx"], capture_at=time, value=row[2])
		sensor_2 = Sensor(user=User(id=uid), sensor_type=sensor_type_dict["magy"], capture_at=time, value=row[3])
		sensor_3 = Sensor(user=User(id=uid), sensor_type=sensor_type_dict["magz"], capture_at=time, value=row[4])
		sensor_list.append(sensor_1) 
		sensor_list.append(sensor_2)
		sensor_list.append(sensor_3)
		#utils_insert_sensor(uid,"magx",row[2],time)
		#utils_insert_sensor(uid,"magy",row[3],time)
		#utils_insert_sensor(uid,"magz",row[4],time)
		return (time, "MAG",{"magx":row[2],"magy":row[3],"magz":row[4]})
	elif label == "CAM":
		value = imagename_2_path(row[2].strip(), uid, time)
		sensor_1 = Sensor(user=User(id=uid), sensor_type=sensor_type_dict["cam"], capture_at=time, value=value)
		sensor_list.append(sensor_1) # Sensor type list [Sensor(user=User(id=uid), sensor_type=sensor_type, capture_at=time, value=value),]
		#utils_insert_sensor(uid,"cam",row[2],time)
		return (time, "CAM",row[2])
	else:
		return (None, None, None)

def utils_batch_insert_sensor_thread():
	"""
	"""
	thread = Thread(target=utils_batch_insert_sensor, args=())
	thread.start()

def utils_batch_insert_picture():
	"""This function batch insert all contents in a sensor file into sensor database table
	
	:param 	sensor_list: file path 
	:type 	file_path: string
	:returns: datetime.date
	"""
	global sensor_list
	try:
		#sensor_type = SensorType.objects.get(abbreviation=abbr)
		#sensor = Sensor(user=User(id=uid), sensor_type=sensor_type, \
		#		capture_at=time, value=value)
		#sensor.save()
		#print "sensor inserted"
		# bulk_create
		print "bulk create sensor list"
		print datetime.now()
		Sensor.objects.bulk_create(sensor_list)
		print "finished bulk create sensor list"
		print datetime.now()
	except IntegrityError:
		print "IntegrityError in utils_insert_sensor"

def utils_batch_insert_picture_thread():
	"""
	"""
	thread = Thread(target=utils_batch_insert_sensor, args=())
	thread.start()

def utils_batch_insert_sensor():
	"""This function batch insert pictures 
	
	:param 	sensor_list: file path 
	:type 	file_path: string
	:returns: datetime.date
	"""
	global sensor_list
	try:
		#sensor_type = SensorType.objects.get(abbreviation=abbr)
		#sensor = Sensor(user=User(id=uid), sensor_type=sensor_type, \
		#		capture_at=time, value=value)
		#sensor.save()
		#print "sensor inserted"
		# bulk_create
		print "bulk create sensor list"
		print datetime.now()
		window_length = 100
		for i in range(1,len(sensor_list)/window_length+2):
			sub_list = sensor_list[(i-1)*window_length:i*window_length]
			if len(sub_list) > 0:
				Sensor.objects.bulk_create(sub_list)
		print "finished bulk create sensor list"
		print datetime.now()
	except IntegrityError:
		print "IntegrityError in utils_insert_sensor"
		

def utils_batch_import_annotation():
	"""This function batch insert all contents in a sensor file into sensor database table
	
	:param 	sensor_list: file path 
	:type 	file_path: string
	:returns: datetime.date
	"""
	try:
		AnnotationAction.objects.bulk_create(annotation_action_list)
	except IntegrityError:
		print "IntegrityError in utils_batch_import_annotation"


def move_sensecam_sensor_file(sensor_capture_date, sensor_file_path):
	"""This function analyze one row of sensor file
			[{"ACC":,"TMP":,"CLR":"PIR":"BAT":"MAG":,"CAM":},{}]
	
	:param 	file_path: file path 
	:type 	file_path: string
	:returns: datetime.date
	"""
	dirname 	= os.path.dirname(sensor_file_path)
	fileName, fileExtension = os.path.splitext(sensor_file_path)
	basename 	= os.path.basename(sensor_file_path)
	dst_filename= "sensor_"+str(sensor_capture_date)+fileExtension
	dst 		= os.path.join(dirname, dst_filename)
	#sensor_2014-05-18.csv
	if os.path.isfile(sensor_file_path):
		shutil.move(sensor_file_path, dst)

	src = "sensor"+sensor_file_path.split('/sensor')[1]+'/'+dst_filename
	dst = "sensor/"+sensor_file_path.split('/sensor/')[1]
	#sensor/user_1/sensor_2014-05-18.csv
	DBHelper.update_sensor_file(src, dst)
	return dst

