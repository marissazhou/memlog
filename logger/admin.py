from django.contrib import admin

from logger.models import *

class InteractionTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description', 'added_by', 'added_at')

class UserInteractionAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'itact_type', 'message', 'created_at')


admin.site.register(InteractionType, InteractionTypeAdmin)
admin.site.register(UserInteraction, UserInteractionAdmin)
