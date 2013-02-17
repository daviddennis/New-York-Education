# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Final'
        db.create_table('app_final', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dbn', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('va_0910_eng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('va_0809_eng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('va_0809_math', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('va_0708_eng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('va_0708_math', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('va_0607_eng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('va_0607_math', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('school_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('teacherid', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('freelunch', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=1, blank=True)),
            ('ell', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=1, blank=True)),
            ('asian', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=1, blank=True)),
            ('black', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=1, blank=True)),
            ('hisp', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=1, blank=True)),
            ('white', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=1, blank=True)),
            ('male', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=1, blank=True)),
            ('female', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=1, blank=True)),
            ('overall_grade', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('dropout', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=1, blank=True)),
            ('va_0910_math', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cohort_category', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('cohort_size', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('grads_num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('grads_percent', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('regents_num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('regents_percent_total', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('regents_percent_grad', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('advregents_num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('advregents_percent_total', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('advregents_percent_grad', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('othregents_num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('othregents_percent_total', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('othregents_percent_grad', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('local_num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('local_percent_total', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('local_percent_grad', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('enrolled_num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('enrolled_percent', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('drop_num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('drop_percent', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('app', ['Final'])


        # Changing field 'School.additional_credit2012'
        db.alter_column('app_school', 'additional_credit2012', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=1))

        # Changing field 'School.perf_category2012'
        db.alter_column('app_school', 'perf_category2012', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=1))

        # Changing field 'School.environ_score'
        db.alter_column('app_school', 'environ_score', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=1))

        # Changing field 'School.peer_index'
        db.alter_column('app_school', 'peer_index', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2))

        # Changing field 'School.prog_score2012'
        db.alter_column('app_school', 'prog_score2012', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=1))

        # Changing field 'School.percent2012'
        db.alter_column('app_school', 'percent2012', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=1))

        # Changing field 'School.score2012'
        db.alter_column('app_school', 'score2012', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=1))

        # Changing field 'School.readiness_score2012'
        db.alter_column('app_school', 'readiness_score2012', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=1))

    def backwards(self, orm):
        # Deleting model 'Final'
        db.delete_table('app_final')


        # Changing field 'School.additional_credit2012'
        db.alter_column('app_school', 'additional_credit2012', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=1))

        # Changing field 'School.perf_category2012'
        db.alter_column('app_school', 'perf_category2012', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1))

        # Changing field 'School.environ_score'
        db.alter_column('app_school', 'environ_score', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1))

        # Changing field 'School.peer_index'
        db.alter_column('app_school', 'peer_index', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2))

        # Changing field 'School.prog_score2012'
        db.alter_column('app_school', 'prog_score2012', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1))

        # Changing field 'School.percent2012'
        db.alter_column('app_school', 'percent2012', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1))

        # Changing field 'School.score2012'
        db.alter_column('app_school', 'score2012', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1))

        # Changing field 'School.readiness_score2012'
        db.alter_column('app_school', 'readiness_score2012', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=1))

    models = {
        'app.demographic': {
            'Meta': {'object_name': 'Demographic'},
            'asian_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'black_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'dbn': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'ell_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'female_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'freelunch_percent': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'freelunch_reduced_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'hispanic_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'male_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'sped_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'white_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        'app.event': {
            'Meta': {'object_name': 'Event'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 17, 0, 0)'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 17, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'app.final': {
            'Meta': {'object_name': 'Final'},
            'advregents_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'advregents_percent_grad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'advregents_percent_total': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'asian': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'black': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'cohort_category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cohort_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dbn': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'drop_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'drop_percent': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dropout': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'ell': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'enrolled_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'enrolled_percent': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'female': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'freelunch': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'grads_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grads_percent': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'hisp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'local_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'local_percent_grad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'local_percent_total': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'male': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'othregents_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'othregents_percent_grad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'othregents_percent_total': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'overall_grade': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'regents_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'regents_percent_grad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'regents_percent_total': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'school_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'teacherid': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'va_0607_eng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'va_0607_math': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'va_0708_eng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'va_0708_math': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'va_0809_eng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'va_0809_math': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'va_0910_eng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'va_0910_math': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'white': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'})
        },
        'app.graduation': {
            'Meta': {'object_name': 'Graduation'},
            'advregents_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'advregents_percent_grad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'advregents_percent_total': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cohort_category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cohort_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dbn': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'drop_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'drop_percent': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'enrolled_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'enrolled_percent': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'grads_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grads_percent': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'local_percent_grad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'local_percent_total': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'othregents_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'othregents_percent_grad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'othregents_percent_total': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'regents_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'regents_percent_grad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'regents_percent_total': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.School']", 'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'app.school': {
            'Meta': {'object_name': 'School'},
            'additional_credit2012': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'dbn': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'environ_grade': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'environ_score': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'grade2012': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'peer_index': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'percent2012': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'perf_category2012': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'perf_grade2012': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'principal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'prog_grade2010': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'prog_grade2011': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'prog_grade2012': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'prog_score2012': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'progress_report_type': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'readiness_grade2012': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'readiness_score2012': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'}),
            'school_level': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'score2012': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '1', 'blank': 'True'})
        },
        'app.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'dbn': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'grade0708': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'grade0809': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'grade0910': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo_url': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True'}),
            'poverty': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True'}),
            'profile_url': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.School']", 'null': 'True'}),
            'school_name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'teacher_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'teacher_name_first_1': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'teacher_name_last_1': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'va_0506': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'va_0607': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'va_0708': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'va_0809': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'va_0910': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'})
        }
    }

    complete_apps = ['app']