import datetime
import json

from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.views.generic.base import View
from django.template import loader, Context
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template.context import RequestContext
from django.contrib.auth.models import User, Group

def index(request):
	"""
	This is the index view for annotater, mainly designed by Brain Moynagh
	"""
	template = loader.get_template('contact/index.html')

	para_view = {}
	context = RequestContext(request, para_view)
	response = template.render(context)
	return HttpResponse(response)

