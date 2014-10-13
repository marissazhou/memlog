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

import os
import datetime
import json
from time import localtime
import os, fnmatch

rename_list = {"device": 'dvar1',
              "end_at": 'eavar1',
              "aaa": '111',
              "bbb": '222',
              "start_at": 'savar1' }


def findReplace(directory, filePattern):
	for path, dirs, files in os.walk(os.path.abspath(directory)):
		for filename in fnmatch.filter(files, filePattern):
			filepath = os.path.join(path, filename)
			with open(filepath) as f:
				s = f.read()
			for find in rename_list:
				replace = rename_list[find]
				s = s.replace(find, replace)
				with open(filepath, "w") as f:
					f.write(s)

if __name__ == "__main__":
	dir = "/var/www/sensecam_browser/docs/tools"
	findReplace(dir, "*.txt")
	findReplace(dir, "*.py")

