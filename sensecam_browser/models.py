from django.db import models
from django.contrib.auth.models import User, Group

# owner field allows for identification of own datasets in more advanced versions
# profile image can be called by {{ object.mug_shot.url }}
# There should be four types of users:
# 	1. Administrator
# 	2. Annotator
# 	3. researcher 
# 	4. subject 
class UserProfile(models.Model):
	user 		= models.ForeignKey(User, unique=True)
   	url 		= models.URLField("Website", blank=True)
   	company 	= models.CharField(max_length=50, blank=True)
	first_name 	= models.CharField(max_length=255, unique=True)
	surname 	= models.CharField(max_length=255, unique=True)
	middle_name = models.CharField(max_length=255, unique=True)
	password 	= models.CharField(max_length=255, unique=True)
	birthday	= models.DateTimeField(auto_now_add=True)
	gender		= models.BooleanField(default=True)
	profile_image	= models.ImageField(upload_to='photos/profile_image/%Y/%m/%d')
	group		= models.ForeignKey(Group, default=1)
	created_at	= models.DateTimeField(auto_now_add=True)
	updated_at	= models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.first_name+ ' ' + self.surname

	class Meta:
		ordering = ['pk']

# Groups of BrowserUsers
class BrowserGroup(models.Model):
	name 		= models.CharField(max_length=100)
	creator		= models.ForeignKey(BrowserUser, default=1)
	description	= models.CharField(max_length=1000)
	created_at	= models.DateTimeField(auto_now_add=True)
	updated_at	= models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['pk']

		
# Event includes in the lifelogs
# This tasks table records which task is assigned to which user mainly for annotation task.
# Only Administrator has the permission to insert into this table.
class Tasks(models.Model):
	user		= models.ForeignKey(User, default=1)
	album		= models.ForeignKey(Album, default=1)
	task_type	= models.IntegerField(default=0)
	description	= models.CharField(max_length=1000)

	#...
	@property
	class Meta:
		unique_together = ('user', 'album', 'task_type')
		ordering 	= ['pk']

	def __unicode__(self):
		return self.user

# User Interaction, itact_type means interaction type, 0:Error, 1:UserClick, 2:warning
class UserInteraction(models.Model):
	creator		= models.ForeignKey(BrowserUser, default=1)
	itact_type  = models.IntegerField(default=0)
	message 	= models.CharField(max_length=100)
	created_at	= models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.creator + ':' + self.itact_type

	class Meta:
		ordering = ['pk']


# Sensor table to store raw sensor data from Sensecam or Autographer
class Sensor(models.Model):
	creator		= models.ForeignKey(BrowserUser, default=1)
	event		= models.ForeignKey(Event, default=1)
	acc_x 		= models.DecimalField('_acc_x_', max_digits=19, decimal_places=9, null=True)
	acc_y 		= models.DecimalField('_acc_y_', max_digits=19, decimal_places=9, null=True)
	acc_z 		= models.DecimalField('_acc_z_', max_digits=19, decimal_places=9, null=True)
	mag_x 		= models.DecimalField('_mag_x_', max_digits=19, decimal_places=9, null=True)
	mag_y 		= models.DecimalField('_mag_y_', max_digits=19, decimal_places=9, null=True)
	mag_z 		= models.DecimalField('_mag_z_', max_digits=19, decimal_places=9, null=True)
	fuel_x 		= models.DecimalField('_fuel_x_', max_digits=19, decimal_places=9, null=True)
	fuel_y 		= models.DecimalField('_fuel_y_', max_digits=19, decimal_places=9, null=True)
	fuel_z 		= models.DecimalField('_fuel_z_', max_digits=19, decimal_places=9, null=True)
	temperature	= models.DecimalField('_temperature_', max_digits=19, decimal_places=9, null=True)
	acc_combined	= models.DecimalField('_acc_combined_', max_digits=19, decimal_places=9, null=True)
	pir_manipulated	= models.DecimalField('_pir_manipulated_', max_digits=19, decimal_places=9, null=True)
	trigger_code	= models.CharField('_trigger_code_', max_length=10, null=True)
	image_address	= models.CharField('_image_address_', max_length=1000, null=True)
	sample_time	= models.CharField('_sample_time_', max_length=100, null=True)
	chunk           = models.IntegerField(default=0)
	white_val       = models.IntegerField(default=0)
	battery         = models.IntegerField(default=0)
	pir	        = models.IntegerField(default=0)

	def __unicode__(self):
		return self.creator

	class Meta:
		ordering = ['pk']

# 
class UserInteraction(models.Model):
	creator		= models.ForeignKey(BrowserUser, default=1)
	itact_type  = models.IntegerField(default=0)
	message 	= models.CharField(max_length=100)
	created_at	= models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.creator + ':' + self.itact_type

	class Meta:
