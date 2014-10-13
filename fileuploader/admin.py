from django.contrib import admin

from models import *

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'capture_date', 'uploaded_at', 'start_at', 'end_at')

class PictureAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'file', 'capture_at', 'uploaded_at', 'updated_at')

class SensorAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'sensor_type', 'value', 'capture_at', 'uploaded_at', 'updated_at')

class SensorTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'abbreviation')

class SensorFileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'file', 'uploaded_at', 'updated_at')

class DeviceTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

admin.site.register(Album, AlbumAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(SensorFile, SensorFileAdmin)
admin.site.register(SensorType, SensorTypeAdmin)
admin.site.register(DeviceType, DeviceTypeAdmin)
