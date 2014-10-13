"""dabatabase manipulation class
.. module:: DBFileUploaderHelper
   :platform: Ubuntu Unix
   :synopsis: A module for conducting all database relavant manipulations.

.. moduleauthor:: Lijuan Marissa Zhou <marissa.zhou.cn@gmail.com>
.. copyright:: copyright reserved 

"""
import unicodedata

from downloader.models import *
from memlog_settings import *
from utils import * 



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
image_folders       = []



def db_downloader_get_researcher_annotated_data(abbr, sensorname):
	"""This function get baseline energy total for bmi 

	:returns: sensor type id in the sensortype table 
	"""
	return None 
