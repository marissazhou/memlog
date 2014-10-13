from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# User Interaction Type, itact_type means interaction type, 0:Error, 1:UserClick, 2:warning
class InteractionType(models.Model):
	name		= models.CharField(max_length=100)
	description	= models.CharField(max_length=100)
	added_by	= models.ForeignKey(User, related_name='added_by')
	added_at	= models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['pk']


# User Interaction, itact_type means interaction type, 0:Error, 1:UserClick, 2:warning
class UserInteraction(models.Model):
	user		= models.ForeignKey(User, related_name='logger')
	itact_type  = models.ForeignKey(InteractionType, default=1)
	message 	= models.CharField(max_length=100)
	created_at	= models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['pk']

