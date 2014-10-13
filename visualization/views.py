from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.template import loader, Context
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import get_messages

#from fileuploader 
import os

@login_required
def index(request):
	"""
	"""
	messages.add_message(request, messages.INFO, 'Hello world.')

	data = {}
	data.update(csrf(request))
	return render_to_response('visualization/index.html', context_instance=RequestContext(request))

@login_required
def scatter(request):
	"""
	"""
	return render_to_response('visualization/scatter.html', context_instance=RequestContext(request))


@login_required
def link(request):
	"""
	"""
	return render_to_response('visualization/linked_data.html', context_instance=RequestContext(request))


@login_required
def timeline(request):
	"""
	"""
	return render_to_response('visualization/timeline.html', context_instance=RequestContext(request))

@login_required
def acc(request):
	"""
	"""
	return render_to_response('visualization/accelerometer.html', context_instance=RequestContext(request))



@login_required
def line(request):
	"""
	"""
	return render_to_response('visualization/linechart.html', context_instance=RequestContext(request))


