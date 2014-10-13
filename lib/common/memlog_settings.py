"""setting class
   This class includes all settings 

.. module:: common 
   :platform: Ubuntu Unix
   :synopsis: A module for all common functions 

.. moduleauthor:: Lijuan Marissa Zhou <marissa.zhou.cn@gmail.com>

"""

'''
 	constants 
'''
#MEDIA_ROOT = '/home/media/sensecambrowser/'
SENSOR_JSON_ROOT = '/home/media/sensecambrowser/sensorjson/'

##################################################
#########	 file size					##########
##################################################
MINIMUM_FILE_SIZE			= 2048 
MAXIMUM_FILE_SIZE			= 1002048 

##################################################
#########	 device type				##########
##################################################
DEVICE_TYPE_AUTOGRAPHER 	= 1	 
DEVICE_TYPE_SENSECAM 		= 2	 
DEVICE_TYPE_VICONREVUE 		= 3	 
DEVICE_TYPE_SENSESEER		= 4	 
DEVICE_TYPE_NARRATIVE		= 5 
DEVICE_TYPE_FUNF			= 6 
DEVICE_TYPE_AUTOGRAPHER_U 	= 7	 
DEVICE_TYPE_SENSECAM_U 		= 8	 
DEVICE_TYPE_VICONREVUE_U	= 9	 
DEVICE_TYPE_SENSESEER_U		= 10	 
DEVICE_TYPE_NARRATIVE_U		= 11 
DEVICE_TYPE_FUNF_U			= 12 

##################################################
#########	 device type				##########
##################################################
LATEST_DATE 				= None

##################################################
#########	 priority levels			##########
##################################################
LOG_TYPE_USER_ANNOTATION	= 0 
LOG_TYPE_USER_OPERATION 	= 1 
LOG_TYPE_USER_WARNING		= 2 

##################################################
#########	sensor abbreviation dict 	##########
##################################################
SENSOR_ABBREVIATION_AUTOGRAPHER = {	'3'	:	'sz', \
									'4'	: 	'typ', \
									'5'	: 	'p', \
									'6'	: 	'accx', \
									'7'	: 	'accy', \
									'8'	: 	'accz', \
									'9'	: 	'magx', \
									'10': 	'magy', \
									'11': 	'magz', \
									'12': 	'red', \
									'13': 	'green', \
									'14': 	'blue', \
									'15': 	'lum', \
									'16': 	'tem', \
									'17': 	'g', \
									'18': 	'lat', \
									'19': 	'lon', \
									'20': 	'alt', \
									'21': 	'gs', \
									'22': 	'herr', \
									'23': 	'verr', \
									'24': 	'exp', \
									'25': 	'gain', \
									'26': 	'rbal', \
									'27': 	'gbal', \
									'28': 	'bbal', \
									'29': 	'xor', \
									'30': 	'yor', \
									'31': 	'zor', \
									'32': 	'stags', \
									'33': 	'tags'}
SENSOR_ABBREVIATION_SENSECAM	= {	'3'	:	'typ', \
									'4'	: 	'p', \
									'32': 	'tags'}
