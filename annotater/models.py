from django.db import models
from django.contrib.auth.models import User

from fileuploader.models import Picture 

# Annotation terms included in the lifelogs
# These terms can be either predefined or user-defined
# User is the one who adds this annotation term
class AnnotationTerm(models.Model):
	concept 			= models.CharField(max_length=100, unique=True, null=False,db_index=True)
	category 			= models.CharField(max_length=100, unique=False, null=False)
	user        		= models.ForeignKey(User, default=1, null=False)
	private				= models.BooleanField(default=False, null=False)
	add_at        		= models.DateTimeField(auto_now_add=True, null=False)

	def __unicode__(self):
		return self.concept

# Annotation action or record
class AnnotationAction(models.Model):
	annotator          	= models.ForeignKey(User, default=1, null=False)
	image            	= models.ForeignKey(Picture, default=1, null=False)
	concept            	= models.ForeignKey(AnnotationTerm, default=1, null=False)
	annotate_at        	= models.DateTimeField(auto_now_add=True, null=False)

	class Meta:
		unique_together = ('image', 'concept')
        index_together = [
                            ['image', 'concept'],
                        ]

# Annotation task
# Assign different subject albums to different annotaters
class AnnotationTask(models.Model):
	assigner          	= models.ForeignKey(User, default=1, related_name="assigners", null=False)
	annotator          	= models.ForeignKey(User, default=1, related_name="annotators", null=False)
	subject          	= models.ForeignKey(User, default=1, related_name="subjects", null=False)
	no_album			= models.IntegerField(default=0, null=False)
	no_image			= models.IntegerField(default=0, null=False)
	finished			= models.BooleanField(default=False, null=False)
	assign_at        	= models.DateTimeField(auto_now_add=True, null=False)
	updated_at  		= models.DateTimeField(auto_now=True, null=False)

	class Meta:
		unique_together = ('annotator', 'subject')
        index_together = [
                            ['annotator', 'subject'],
                        ]
