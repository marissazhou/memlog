from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


# TODO: 
class CoheAuthenticationForm(AuthenticationForm):
	#Sign_In_As = forms.ChoiceField(choices=[(x, x) for x in ['Subject', 'Administrator', 'Researcher', 'Annotator']])
	# group = forms.ModelChoiceField(queryset=Group.objects, required=True, empty_label="(No Group)")

	def __init__(self, *args, **kwargs):
		super(CoheAuthenticationForm, self).__init__(*args, **kwargs)

		self.base_fields['username'].widget.attrs['class'] = 'form-control'
		self.base_fields['username'].widget.attrs['placeholder'] = 'Username'

		self.base_fields['password'].widget.attrs['class'] = 'form-control'
		self.base_fields['password'].widget.attrs['placeholder'] = 'Password'
		
		#self.base_fields['group'].widget.attrs['style'] = 'display: none;'
		#self.base_fields['group'].widget.attrs['placeholder'] = 'Group'


class CoheUserRegistrationForm(UserCreationForm):
    Group = forms.ModelChoiceField(queryset=Group.objects, required=True)
