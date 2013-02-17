from django.db import models
from datetime import datetime

# Create your models here.
class Event(models.Model):
	title = models.CharField(max_length=500)
	address = models.CharField(max_length=500)
	description = models.TextField()
	date = models.DateTimeField(default=datetime.now())
	created_at = models.DateTimeField(default=datetime.now())

class School(models.Model):
    dbn = models.CharField(max_length=10)
    district = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    principal = models.CharField(max_length=100)
    progress_report_type = models.CharField(max_length=5)
    school_level = models.CharField(max_length=30)
    peer_index = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    grade2012 = models.CharField(max_length=1, blank=True)
    score2012 = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    percent2012 = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    prog_score2012 = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    prog_grade2012 = models.CharField(max_length=1, blank=True)
    perf_category2012 = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    perf_grade2012 = models.CharField(max_length=1, blank=True)
    environ_score = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    environ_grade = models.CharField(max_length=1, blank=True)
    readiness_score2012 = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    readiness_grade2012 = models.CharField(max_length=1, blank=True)
    additional_credit2012 = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    prog_grade2011 = models.CharField(max_length=1, blank=True)
    prog_grade2010 = models.CharField(max_length=1, blank=True)

    def __unicode__(self):
        return self.name

class Teacher(models.Model):
    dbn = models.CharField(max_length=10)
    school_name = models.CharField(max_length=500)
    teacher_name_first_1 = models.CharField(max_length=500)
    teacher_name_last_1 = models.CharField(max_length=500)
    grade0708 = models.CharField(max_length=100, blank=True, null=True)
    grade0809 = models.CharField(max_length=100, blank=True, null=True)
    grade0910 = models.CharField(max_length=100, blank=True, null=True)
    va_0506 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    va_0607 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    va_0708 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    va_0809 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    va_0910 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    description = models.TextField(null=True)
    photo_url = models.CharField(max_length=300, null=True)
    poverty = models.CharField(max_length=300, null=True)
    profile_url = models.CharField(max_length=300, null=True)

    teacher_id = models.IntegerField(blank=True, null=True)

    school = models.ForeignKey(School, null=True)

    def name(self):
    	return '%s %s' % (self.teacher_name_first_1.capitalize(), self.teacher_name_last_1.capitalize())

class Graduation(models.Model):
    dbn = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    year = models.IntegerField(blank=True, null=True)
    cohort_category = models.CharField(max_length=30)
    cohort_size = models.IntegerField(blank=True, null=True)
    grads_num = models.IntegerField(blank=True, null=True)
    grads_percent = models.CharField(max_length=30)
    regents_num = models.IntegerField(blank=True, null=True)
    regents_percent_total = models.CharField(max_length=30)
    regents_percent_grad = models.CharField(max_length=30)
    advregents_num = models.IntegerField(blank=True, null=True)
    advregents_percent_total = models.CharField(max_length=30)
    advregents_percent_grad = models.CharField(max_length=30)
    othregents_num = models.IntegerField(blank=True, null=True)
    othregents_percent_total = models.CharField(max_length=30)
    othregents_percent_grad = models.CharField(max_length=30)
    local_num = models.IntegerField(blank=True, null=True)
    local_percent_total = models.CharField(max_length=30)
    local_percent_grad = models.CharField(max_length=30)
    enrolled_num = models.IntegerField(blank=True, null=True)
    enrolled_percent = models.CharField(max_length=30)
    drop_num = models.IntegerField(blank=True, null=True)
    drop_percent = models.CharField(max_length=30)

    school = models.ForeignKey(School, null=True)

class Demographic(models.Model):
	dbn = models.CharField(max_length=10, blank=True)
	name = models.CharField(max_length=100, blank=True)
	year = models.CharField(max_length=30, blank=True)
	freelunch_percent = models.CharField(max_length=30, null=True)
	freelunch_reduced_percent = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
	ell_percent = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
	sped_percent = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
	asian_percent = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
	black_percent = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
	hispanic_percent = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
	white_percent = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
	male_percent = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
	female_percent = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)





