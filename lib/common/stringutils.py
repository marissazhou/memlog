"""stringutils include utilities to process strings 
   This module includes:
   	1. String process functions for annotation and sensor imports
	2. 

.. module:: common 
   :platform: Ubuntu Unix
   :synopsis: A module for string processing 

.. moduleauthor:: Lijuan Marissa Zhou <marissa.zhou.cn@gmail.com>

"""

'''
	PACKAGES
'''
import json
import csv
import scipy
from datetime import datetime, date, time
'''
	MODELS
'''

'''
 	CONSTRAINTS	
'''

def annotation_import_get_annotation(str_annotation):
    """This function extract annotation from annotation string in exported annotation files from the old sensecam browser system
    
    :param extention: 
    :type extention: 
    :returns: 
    """
    if str_annotation == 'NULL':
		return str_annotation
    annotation = str_annotation.split(".")[2].strip()
    return annotation

def imagename_2_path(imagename, uid, capture_at):
    """This function convert imagename and compound information to relative picture file path like in the database
    
    :param extention: 
    :type extention: 
    :returns: 
    """
    path = "img/user_"+str(uid)+"/"+str(capture_at.year)+"/"+str(capture_at.month)+"/"+str(capture_at.day)+"/"+imagename
    return path
