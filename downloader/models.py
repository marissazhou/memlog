from django.db import models
from django.contrib.auth.models import User

# the following is to save files into a specified folder 
# for that authenticated user
# unique together ensures the same image of the same user wont be stored twice
class ResearcherData(models.Model):
	capture_at  = models.DateTimeField(auto_now_add=False)
	uploaded_at = models.DateTimeField(auto_now_add=True)
	updated_at  = models.DateTimeField(auto_now=True)
	visible		= models.BooleanField(default=True)

	class Meta:
		unique_together = ('capture_at', )
