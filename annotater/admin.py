from django.contrib import admin

from models import *

class AnnotationTermAdmin(admin.ModelAdmin):
	list_display = ('id', 'concept', 'category', 'user', 'private', 'add_at')

class AnnotationActionAdmin(admin.ModelAdmin):
	list_display = ('id', 'annotator', 'concept', 'annotate_at')

class AnnotationTaskAdmin(admin.ModelAdmin):
	list_display = ('id', 'assigner', 'annotator', 'subject', 'no_album', 'no_image', 'finished', 'assign_at')

admin.site.register(AnnotationTerm, AnnotationTermAdmin)
admin.site.register(AnnotationAction, AnnotationActionAdmin)
admin.site.register(AnnotationTask, AnnotationTaskAdmin)
