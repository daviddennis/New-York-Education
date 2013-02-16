# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.x'
        db.add_column('app_event', 'x',
                      self.gf('django.db.models.fields.TextField')(default='ds'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.x'
        db.delete_column('app_event', 'x')


    models = {
        'app.event': {
            'Meta': {'object_name': 'Event'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'blah': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'clah': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 16, 0, 0)'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 16, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'x': ('django.db.models.fields.TextField', [], {'default': "'ds'"})
        }
    }

    complete_apps = ['app']