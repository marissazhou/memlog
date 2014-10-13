"""dabatabase manipulation class
.. module:: authHelper
   :platform: Ubuntu Unix
   :synopsis: A module for conducting all database annotater.

.. moduleauthor:: Lijuan Marissa Zhou <marissa.zhou.cn@gmail.com>
.. copyright:: copyright reserved 

"""
import unicodedata
from datetime import datetime

from utils import *
from time import gmtime, strftime

from auth.models import *
from django.contrib.auth.models import User, Group
from django.db.models import Q 

def db_auth_all_group_users(group_name):
	"""This function get all users belonging to a users group 

	:param group_name: group name 
	:type group_name: string 
	:returns: users list
	"""
	users 			= []
	#group 			= Group.objects.get(id=gid)
	users_queryset = User.objects.all().filter(groups__name=group_name).values("id")
	return users_queryset 

def db_auth_all_group_users_annotation(group_name):
	"""This function get all users belonging to a users group 

	:param group_name: group name 
	:type group_name: string 
	:returns: users list
	"""
	users_queryset 	= db_auth_all_group_users(group_name)
	users 			= []
	for user in users_queryset:
		uid 	= user["id"]
		alias 	= group_name+"_"+str(uid)
		users.append({"id":uid,"alias":alias})
	return users

