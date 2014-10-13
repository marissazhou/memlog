from django.contrib import admin

from models import *

class PhysicalActivityTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'category', 'user', 'private', 'add_at')

class PhysicalActivityAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'pa_type', 'start_time', 'end_time', 'steps', 'distance', 'energy_expenditure', 'added_at')

admin.site.register(PhysicalActivityType, PhysicalActivityTypeAdmin)
admin.site.register(PhysicalActivity, PhysicalActivityAdmin)
