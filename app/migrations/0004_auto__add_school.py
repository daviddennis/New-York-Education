# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'School'
        db.create_table('app_school', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dbn', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('principal', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('progress_report_type', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('school_level', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('peer_index', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('grade2012', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('score2012', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1, blank=True)),
            ('percent2012', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1, blank=True)),
            ('prog_score2012', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1, blank=True)),
            ('prog_grade2012', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('perf_category2012', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1, blank=True)),
            ('perf_grade2012', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('environ_score', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1, blank=True)),
            ('environ_grade', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('readiness_score2012', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=1, blank=True)),
            ('readiness_grade2012', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('additional_credit2012', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=1, blank=True)),
            ('prog_grade2011', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('prog_grade2010', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('app', ['School'])


    def backwards(self, orm):
        # Deleting model 'School'
        db.delete_table('app_school')


    models = {
        'app.event': {
            'Meta': {'object_name': 'Event'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 16, 0, 0)'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 16, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'app.school': {
            'Meta': {'object_name': 'School'},
            'additional_credit2012': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'dbn': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'environ_grade': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'environ_score': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'grade2012': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'peer_index': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'percent2012': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'perf_category2012': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'perf_grade2012': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'principal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'prog_grade2010': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'prog_grade2011': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'prog_grade2012': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'prog_score2012': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'progress_report_type': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'readiness_grade2012': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'readiness_score2012': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'school_level': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'score2012': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'})
        }
    }

    complete_apps = ['app']