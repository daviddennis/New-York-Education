# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Event.blah'
        db.delete_column('app_event', 'blah')

        # Deleting field 'Event.clah'
        db.delete_column('app_event', 'clah')

        # Deleting field 'Event.x'
        db.delete_column('app_event', 'x')


    def backwards(self, orm):
        # Adding field 'Event.blah'
        db.add_column('app_event', 'blah',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300),
                      keep_default=False)

        # Adding field 'Event.clah'
        db.add_column('app_event', 'clah',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300),
                      keep_default=False)

        # Adding field 'Event.x'
        db.add_column('app_event', 'x',
                      self.gf('django.db.models.fields.TextField')(default='ds'),
                      keep_default=False)


    models = {
        'app.event': {
            'Meta': {'object_name': 'Event'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 16, 0, 0)'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 16, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['app']