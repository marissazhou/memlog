from django.contrib import admin

from models import *

class EventAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'start_at', 'end_at', 'location')

class EventImageAdmin(admin.ModelAdmin):
	list_display = ('id', 'image', 'event')

admin.site.register(Event, EventAdmin)
admin.site.register(EventImage, EventImageAdmin)
