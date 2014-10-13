#!/usr/bin/env python
# -*- coding: ascii -*-

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = 'Lijuan Marissa Zhou (marissa.zhou.cn@gmail.com)'
__copyright__ = 'Copyright (c) 2011-2014 Lijuan Marissa Zhou'
__license__ = 'License, see LICENSE for more details'
__vcs_id__ = '$Id$'
__version__ = '0.1' #Versioning: http://www.python.org/dev/peps/pep-0386/

"""
Things to do
"""

import datetime
import json

def authentication_processor(request):
    # define a group called annotater
    user = request.user
    # annotater_group = Group(name="annotater")
    # group_name_annotater = "annotater"

    ##########################################
    #### data to be presented ################
    ##########################################
    username    = 'anonymous'
    uid         = 3
    if user.is_authenticated():
        username    = user.username
        uid         = user.id
	return {'username': username,'uid': uid}
