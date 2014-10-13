# Create your views here.

import datetime

from django.http import HttpResponse
from django.views.generic.base import View
from django.template import loader, Context
from django.shortcuts import render_to_response, get_object_or_404
import json
from django.core.context_processors import csrf


def index(request):
        template = loader.get_template('index.html')
        para_view = {}
        context = Context(para_view)
        response = template.render(context)
        return HttpResponse(response)

