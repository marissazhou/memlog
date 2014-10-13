#!/usr/bin/env python
# -*- coding: ascii -*-

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = 'Lijuan Marissa Zhou(marissa.zhou.cn@gmail.com)'
__copyright__ = 'Copyright (c) 2011-2014 Lijuan Marissa Zhou'
__license__ = 'License, see LICENSE for more details'
__vcs_id__ = '$Id$'
__version__ = '0.1' #Versioning: http://www.python.org/dev/peps/pep-0386/

"""
Things to do
"""

import os
import sys

new_path_common = sys.path[0]+'/lib/common'
if new_path_common not in sys.path:
        sys.path.append(new_path_common)
new_path_lib = sys.path[0]+'/lib'
if new_path_lib not in sys.path:
        sys.path.append(new_path_lib)
new_path_logic = sys.path[0]+'/lib/logic'
if new_path_logic not in sys.path:
        sys.path.append(new_path_logic)
new_path_common_db = sys.path[0]+'/lib/common/db'
if new_path_common_db not in sys.path:
        sys.path.append(new_path_common_db)


from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.template import loader, Context
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.models import User

from datetime import date, datetime

#from fileuploader 
from utils import * 
from memlog_settings import *
from sensor import * 
from image import * 
from downloaderHelper import * 
from forms import * 

"""
	global variables
"""
image_ids 			= {} 
sensor_file_path	= None 
album_date			= None 
album_start_time	= None 
album_end_time		= None 
cur_album			= None 
image_folders		= []

@csrf_exempt
@login_required
def index(request):
	"""
	"""
	global image_ids 
	data = {}
	data.update(csrf(request))
	return render_to_response('downloader/index.html', data, context_instance=RequestContext(request))

def researcher():
	"""
	"""
	global image_ids 
	data = {}
	data.update(csrf(request))
	return render_to_response('downloader/researcher.html', data, context_instance=RequestContext(request))
