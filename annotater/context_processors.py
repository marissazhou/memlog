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

def is_annotator_processor(request):
	is_annotator = request.user.groups.filter(name='annotator')
	if len(is_annotator) > 0:
		is_annotator = 1
	else:
		is_annotator = 0
	return {'is_annotator': is_annotator}
