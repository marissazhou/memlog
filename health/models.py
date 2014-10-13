from django.db import models
from django.contrib.auth.models import User

from fileuploader.models import Picture 

# Physical Activities
class PhysicalActivityType(models.Model):
	name	 			= models.CharField(max_length=100, unique=True, null=False)
	category 			= models.CharField(max_length=100, unique=False, null=False)
	user        		= models.ForeignKey(User, default=1, null=False)
	private				= models.BooleanField(default=False, null=False)
	add_at        		= models.DateTimeField(auto_now_add=True, null=False)

	def __unicode__(self):
		return self.name

# Physical Activities
# all activities of all users with energy expenditure
class PhysicalActivity(models.Model):
	user        		= models.ForeignKey(User, default=1, null=False)
	pa_type        		= models.ForeignKey(PhysicalActivityType, default=1, null=False)
	start_time 			= models.DateTimeField(auto_now_add=False, null=False)
	end_time 			= models.DateTimeField(auto_now_add=False, null=False)
	steps				= models.IntegerField(default=1)
	distance			= models.DecimalField(max_digits=19, decimal_places=2)
	energy_expenditure	= models.DecimalField(max_digits=19, decimal_places=2)
	added_at        	= models.DateTimeField(auto_now_add=True, null=False)
