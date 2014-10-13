import os
import sys
sys.path.append('/var/www/sensecam_browser/lib')
sys.path.append('/var/www/sensecam_browser/lib/logic')

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.template import loader, Context
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import threading

# import EventSegmentation
from EventSegmentation import EventSegmentation 
from eventseg import * 
from models import Event 
from models import EventImage

@login_required
def index(request):
	"""
	If there is at least one event, store event info into database and present the latest events in the day view 
	Else there is none event is segmented, present the last latest event day

	Can event segmentation be a different thread, which will not affect the user interface, after the event segmentation is finished, the user will be given an notice saying it is finished and whether to jump to event view.
	"""
	#start event segmentation
	sensor_path = '/home/marissa/Documents/Autographer_lifelog/marissa_lifelog/2013/12/image_table.txt'
	logged_user = request.user
	messages.add_message(request, messages.INFO, 'Hello world.')

	# ------------------------to do------------------------
	# How to make this multithread
	# How to connect to progressbar to tell users this is to be finished 
	# Start segment event, Here should be multi threading
	# this process should start after upload
	t = threading.Thread(target=EventSegmentation(logged_user,sensor_path), args = ())
	t.daemon = True
	t.start()
	while True:
		if not t.isAlive():
			#update events to be the latest
			events = Event.objects.all()
			print "event segmentation is finished"
			return HttpResponseRedirect('event/')
		else:
			print "event segmentation is alive"
			return HttpResponseRedirect('')
	else:
		print 'else'

	#data = {'form_upload': form}	
	#This is when it is the page is firstly visited without any further operation on the pate
	data = {}
	return render_to_response('eventseg/index.html', data, context_instance=RequestContext(request))

@login_required
def event(request):
	"""
        View the details of one event
	"""
	#data = {'form_upload': form}	
	data = {}
	return render_to_response('eventseg/event.html', data, context_instance=RequestContext(request))
