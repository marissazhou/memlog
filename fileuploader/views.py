from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.template import loader, Context
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

#from fileuploader 
from fileuploader import * 
from forms import * 

def index_bk(request):
	template 	= loader.get_template('fileuploader/index.html')
        para_view 	= {}
	#Django comes with a special Context class, django.template.RequestContext, that acts slightly differently than the normal django.template.Context. The first difference is that it takes an HttpRequest as its first argument.
        context 	= RequestContext(request, para_view)
        response 	= template.render(context)
        return HttpResponse(response)

@login_required
def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
			# handle_uploaded_file has not been implemented yet
            #handle_uploaded_file(request.FILES['file'])
            new_file = UploadFile(file = request.FILES['file'])
            new_file.save()
			# in the future, may pop up the page to tell user all files have been uploaded, you can go to my lifelog to view all your events etc..
            #return HttpResponseRedirect('/success/url/')
            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = UploadFileForm()
    data = {'form': form}
    return render_to_response('fileuploader/index.html', data, context_instance=RequestContext(request))
