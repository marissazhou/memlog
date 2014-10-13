# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SensorType'
        db.create_table(u'fileuploader_sensortype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='sensor_type', unique=True, max_length=100)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(default='st', unique=True, max_length=10, db_index=True)),
        ))
        db.send_create_signal(u'fileuploader', ['SensorType'])

        # Adding model 'DeviceType'
        db.create_table(u'fileuploader_devicetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='device_name', unique=True, max_length=100, db_index=True)),
            ('add_by_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(default='st', unique=True, max_length=10)),
        ))
        db.send_create_signal(u'fileuploader', ['DeviceType'])

        # Adding model 'Album'
        db.create_table(u'fileuploader_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('device', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fileuploader.DeviceType'])),
            ('start_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('capture_date', self.gf('django.db.models.fields.DateField')()),
            ('annotation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('uploaded_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'fileuploader', ['Album'])

        # Adding index on 'Album', fields ['user', 'capture_date']
        db.create_index(u'fileuploader_album', ['user_id', 'capture_date'])

        # Adding model 'Picture'
        db.create_table(u'fileuploader_picture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fileuploader.Album'], null=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('resized', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('year', self.gf('django.db.models.fields.CharField')(default='2014', max_length=4)),
            ('month', self.gf('django.db.models.fields.CharField')(default='01', max_length=2)),
            ('day', self.gf('django.db.models.fields.CharField')(default='01', max_length=2)),
            ('capture_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('uploaded_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('codable', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'fileuploader', ['Picture'])

        # Adding unique constraint on 'Picture', fields ['user', 'file']
        db.create_unique(u'fileuploader_picture', ['user_id', 'file'])

        # Adding index on 'Picture', fields ['user', 'album', 'file']
        db.create_index(u'fileuploader_picture', ['user_id', 'album_id', 'file'])

        # Adding model 'Sensor'
        db.create_table(u'fileuploader_sensor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('sensor_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fileuploader.SensorType'])),
            ('value', self.gf('django.db.models.fields.CharField')(default='0', max_length=100)),
            ('capture_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('uploaded_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'fileuploader', ['Sensor'])

        # Adding unique constraint on 'Sensor', fields ['user', 'sensor_type', 'capture_at']
        db.create_unique(u'fileuploader_sensor', ['user_id', 'sensor_type_id', 'capture_at'])

        # Adding model 'SensorJsonFile'
        db.create_table(u'fileuploader_sensorjsonfile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fileuploader.SensorType'])),
            ('capture_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('uploaded_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'fileuploader', ['SensorJsonFile'])

        # Adding unique constraint on 'SensorJsonFile', fields ['user', 'file']
        db.create_unique(u'fileuploader_sensorjsonfile', ['user_id', 'file'])

        # Adding model 'SensorFile'
        db.create_table(u'fileuploader_sensorfile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('capture_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('uploaded_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'fileuploader', ['SensorFile'])

        # Adding unique constraint on 'SensorFile', fields ['user', 'file']
        db.create_unique(u'fileuploader_sensorfile', ['user_id', 'file'])

        # Adding model 'FunfSensorFile'
        db.create_table(u'fileuploader_funfsensorfile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('capture_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('uploaded_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'fileuploader', ['FunfSensorFile'])


    def backwards(self, orm):
        # Removing unique constraint on 'SensorFile', fields ['user', 'file']
        db.delete_unique(u'fileuploader_sensorfile', ['user_id', 'file'])

        # Removing unique constraint on 'SensorJsonFile', fields ['user', 'file']
        db.delete_unique(u'fileuploader_sensorjsonfile', ['user_id', 'file'])

        # Removing unique constraint on 'Sensor', fields ['user', 'sensor_type', 'capture_at']
        db.delete_unique(u'fileuploader_sensor', ['user_id', 'sensor_type_id', 'capture_at'])

        # Removing index on 'Picture', fields ['user', 'album', 'file']
        db.delete_index(u'fileuploader_picture', ['user_id', 'album_id', 'file'])

        # Removing unique constraint on 'Picture', fields ['user', 'file']
        db.delete_unique(u'fileuploader_picture', ['user_id', 'file'])

        # Removing index on 'Album', fields ['user', 'capture_date']
        db.delete_index(u'fileuploader_album', ['user_id', 'capture_date'])

        # Deleting model 'SensorType'
        db.delete_table(u'fileuploader_sensortype')

        # Deleting model 'DeviceType'
        db.delete_table(u'fileuploader_devicetype')

        # Deleting model 'Album'
        db.delete_table(u'fileuploader_album')

        # Deleting model 'Picture'
        db.delete_table(u'fileuploader_picture')

        # Deleting model 'Sensor'
        db.delete_table(u'fileuploader_sensor')

        # Deleting model 'SensorJsonFile'
        db.delete_table(u'fileuploader_sensorjsonfile')

        # Deleting model 'SensorFile'
        db.delete_table(u'fileuploader_sensorfile')

        # Deleting model 'FunfSensorFile'
        db.delete_table(u'fileuploader_funfsensorfile')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'fileuploader.album': {
            'Meta': {'object_name': 'Album', 'index_together': "[['user', 'capture_date']]"},
            'annotation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'capture_date': ('django.db.models.fields.DateField', [], {}),
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fileuploader.DeviceType']"}),
            'end_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_at': ('django.db.models.fields.DateTimeField', [], {}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'fileuploader.devicetype': {
            'Meta': {'object_name': 'DeviceType'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'default': "'st'", 'unique': 'True', 'max_length': '10'}),
            'add_by_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'device_name'", 'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        },
        u'fileuploader.funfsensorfile': {
            'Meta': {'object_name': 'FunfSensorFile'},
            'capture_at': ('django.db.models.fields.DateTimeField', [], {}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'fileuploader.picture': {
            'Meta': {'unique_together': "(('user', 'file'),)", 'object_name': 'Picture', 'index_together': "[['user', 'album', 'file']]"},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fileuploader.Album']", 'null': 'True'}),
            'capture_at': ('django.db.models.fields.DateTimeField', [], {}),
            'codable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'day': ('django.db.models.fields.CharField', [], {'default': "'01'", 'max_length': '2'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.CharField', [], {'default': "'01'", 'max_length': '2'}),
            'resized': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'default': "'2014'", 'max_length': '4'})
        },
        u'fileuploader.sensor': {
            'Meta': {'unique_together': "(('user', 'sensor_type', 'capture_at'),)", 'object_name': 'Sensor'},
            'capture_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fileuploader.SensorType']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'value': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '100'})
        },
        u'fileuploader.sensorfile': {
            'Meta': {'unique_together': "(('user', 'file'),)", 'object_name': 'SensorFile'},
            'capture_at': ('django.db.models.fields.DateTimeField', [], {}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'fileuploader.sensorjsonfile': {
            'Meta': {'unique_together': "(('user', 'file'),)", 'object_name': 'SensorJsonFile'},
            'capture_at': ('django.db.models.fields.DateTimeField', [], {}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fileuploader.SensorType']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'fileuploader.sensortype': {
            'Meta': {'object_name': 'SensorType'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'default': "'st'", 'unique': 'True', 'max_length': '10', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'sensor_type'", 'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['fileuploader']