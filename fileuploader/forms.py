from django import forms
#from models import UploadFile
from models import * 

class UploadFileForm(forms.ModelForm):
#	title = forms.CharField(max_length=50)
#   file  = forms.FileField()
	class Meta:
		model = Picture 

