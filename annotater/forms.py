from django import forms
from models import AnnotationTerm

class AddTermForm(forms.ModelForm):
#	title = forms.CharField(max_length=50)
#   file  = forms.FileField()
	class Meta:
		model = AnnotationTerm

