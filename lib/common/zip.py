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

def (albums, album_ids, date_info, uid):
    """This function move files from one place to another place 
    
    :param albums: directory address string 
    :type albums: string 
    :returns: file address list 
    """
    #print "&&&&&&&&&&&&&& move_files &&&&&&&&&&&&&&&&&&" 
    addresses = [] # [[0,1]]
    dates = albums.keys()
