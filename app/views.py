from django.http import HttpResponse
from django.shortcuts import render
import os, traceback, sys
from app.models import Event, School, Teacher, Graduation, Demographic
from django.core import serializers
import requests, json


def index(request):

	events = Event.objects.all()

	return render(
    	request,
    	'index.html',
    	{'events': events})

# def dump(request):
# 	f = open('data/dump.csv')
# 	teachers = Teacher.objects.all()
# 	for t in teachers:
# 		items = []
# 		items += [
# 			t.va_0910,
# 			t.dbn]

# 	return render(
# 		request,
# 		'index.html')

def home(request, dbn=None, teacher_id=None):

	school = None
	teacher = None


	schools = School.objects.all()
	teachers = []
	if dbn:
		teachers = Teacher.objects.filter(dbn=dbn).order_by('teacher_name_first_1').all()
		school = School.objects.filter(dbn=dbn)[0]

	if teacher_id:
		teacher = Teacher.objects.filter(teacher_id=teacher_id)[0]
		print teacher.name


	s = {'teachers': teachers,
    	'schools': schools}

	if school:
		s['school'] = school

	if teacher:
		s['teacher'] = teacher

	if dbn:
		s['dbn'] = dbn

	return render(
    	request,
    	'analyze.html',
    	s)


def analyze(request, teacher_id):

	teacher = Teacher.objects.filter(id=teacher_id)
	str_request = ('http://api.donorschoose.org/common/json-teacher.html?teacher=%s&APIKey=DONORSCHOOSE' % teacher_id)
	r = requests.get(str_request)
	data_dict = {}
	if r.status_code == 200:
		json_response = json.loads(str(r.text))
		if not teacher:
			teacher = Teacher(id=teacher_id)
		teacher.description = json_response['description']
		teacher.photo_url = json_response['photoURL']
		teacher.poverty = json_response['povertyLevel']
		teacher.profile_url = json_response['profileURL']
		teacher.save()

	return render(
    	request,
    	'analyze.html',
    	{'teacher': teacher})

def load(request):
	# School.objects.all().delete()
	# f = open('data/schools.csv')
	# for line in f.readlines()[3:]:
	# 	cols = [item for item in line.split(',')][1:]
	# 	s = School(
	# 		dbn=cols[0][:10],
	# 		district=cols[1][:2],
	# 		name=cols[2][:100],
	# 		principal=cols[3][:100],
	# 		progress_report_type=cols[4][:5],
	# 		school_level=cols[5][:30])#,
	# 		# peer_index=float(cols[6] or 0),
	# 		# grade2012=cols[7][:1])#,
	# 		# score2012=(float(cols[8][:5] or 0) if ,
	# 		# percent2012=float(cols[9][:5] or 0),
	# 		# prog_score2012=float(cols[10][:5] or 0),
	# 		# prog_grade2012=cols[11][:1])#,
	# 		# perf_category2012=float(cols[12][:5] or 0))#,
	# 		# perf_grade2012=cols[13][:5],
	# 		# environ_score=cols[14][:5],
	# 		# environ_grade=cols[15][:5],
	# 		# readiness_score2012=cols[16][:5])#,
	# 		# readiness_grade2012=cols[17][:5],
	# 		# additional_credit2012=cols[18][:5],
	# 		# prog_grade2011=cols[19][:5],
	# 		# prog_grade2010=cols[20][:5])
	# 	try:
	# 		s.save()
	# 	except:
	# 		print traceback.print_exc(file=sys.stdout)

	Teacher.objects.all().delete()
	f2 = open('data/teachers_matched.csv')
	for line in f2.readlines()[1:]:
		cols = [item for item in line.split(',')][1:]
		t = Teacher()
		t.teacher_name_first_1 = ''.join([c for c in cols[0] if c != '"'])
		t.teacher_name_last_1 = ''.join([c for c in cols[1] if c != '"'])
		if cols[2] != 'NA':
			t.teacher_id = cols[2]
		t.dbn = ''.join([c for c in cols[-10] if c != '"'])

		# t.dbn = ''.join([c for c in cols[0][:10] if c != '"'])
		# t.school_name = cols[1]
		# t.teacher_name_first_1 = ''.join([c for c in cols[2] if c != '"'])
		# t.teacher_name_last_1 = ''.join([c for c in cols[3] if c != '"'])
		# t.grade0708 = cols[-12]
		# t.grade0809 = cols[-11]
		# t.grade0910 = cols[-10]
		# t.va_0506 = clean_num(cols[-5])
		# t.va_0607 = clean_num(cols[-4])
		# t.va_0708 = clean_num(cols[-3])
		# t.va_0809 = clean_num(cols[-2])
		# if cols[15] not in ('NA\n', 'NA'):
		# 	t.va_0910 = cols[-1]
		# s_list = School.objects.filter(dbn=t.dbn)
		# if s_list:
		# 	t.school = s_list[0]
		try:
			t.save()
		except:
			print traceback.print_exc(file=sys.stdout)

	# Graduation.objects.all().delete()
	# f3 = open('data/grads.csv')
	# for line in f3.readlines():
	# 	cols = [item for item in line.split(',')]
	# 	g = Graduation()
	# 	g.dbn = ''.join([c for c in cols[0][:10] if c != '"'])
	# 	g.name = cols[1]
	# 	g.grads_percent = cols[6].replace('%','')
	# 	s_list = School.objects.filter(dbn=g.dbn)
	# 	if s_list:
	# 		g.school = s_list[0]
	# 	try:
	# 		g.save()
	# 	except:
	# 		print traceback.print_exc(file=sys.stdout)

	# Demographic.objects.all().delete()
	# f4 = open('data/demo.csv')
	# for line in f4.readlines()[1:]:
	# 	cols = [item for item in line.split(',')]
	# 	d = Demographic()
	# 	d.dbn = ''.join([c for c in cols[0][:10] if c != '"'])
	# 	d.name = cols[1]
	# 	d.year = cols[2]
	# 	#d.freelunch_reduced_percent = float(cols[4] or 0)
	# 	# d.black_percent = cols[8]
	# 	try:
	# 		d.save()
	# 	except:
	# 		print traceback.print_exc(file=sys.stdout)

	# schools = School.objects.all()
	# teachers = Teacher.objects.all()
	# grads = Graduation.objects.all()
	return render(
    	request,
    	'index.html')
	# ,
 #    	{'schools': schools,
 #    	'teachers': teachers,
 #    	'grads': grads})

def clean_num(s):
	if s in ('NA', 'NA\n', '', None):
		return None
	else:
		return s

	# dbn = models.CharField(max_length=10, blank=True)
 #    name = models.CharField(max_length=100, blank=True)
 #    year = models.CharField(max_length=30, blank=True)
 #    freelunch_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    freelunch_reduced_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    ell_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    sped_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    asian_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    black_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    hispanic_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    white_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    male_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
 #    female_percent = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    # dbn = models.CharField(max_length=10)
    # name = models.CharField(max_length=100)
    # year = models.IntegerField(blank=True, null=True)
    # cohort_category = models.CharField(max_length=30)
    # cohort_size = models.IntegerField(blank=True, null=True)
    # grads_num = models.IntegerField(blank=True, null=True)
    # grads_percent = models.CharField(max_length=30)
    # regents_num = models.IntegerField(blank=True, null=True)
    # regents_percent_total = models.CharField(max_length=30)
    # regents_percent_grad = models.CharField(max_length=30)
    # advregents_num = models.IntegerField(blank=True, null=True)
    # advregents_percent_total = models.CharField(max_length=30)
    # advregents_percent_grad = models.CharField(max_length=30)
    # othregents_num = models.IntegerField(blank=True, null=True)
    # othregents_percent_total = models.CharField(max_length=30)
    # othregents_percent_grad = models.CharField(max_length=30)
    # local_num = models.IntegerField(blank=True, null=True)
    # local_percent_total = models.CharField(max_length=30)
    # local_percent_grad = models.CharField(max_length=30)
    # enrolled_num = models.IntegerField(blank=True, null=True)
    # enrolled_percent = models.CharField(max_length=30)
    # drop_num = models.IntegerField(blank=True, null=True)
    # drop_percent = models.CharField(max_length=30)


    # school_name = models.CharField(max_length=500)
    # teacher_name_first_1 = models.CharField(max_length=500)
    # teacher_name_last_1 = models.CharField(max_length=500)

    # name = models.CharField(max_length=100)
    # principal = models.CharField(max_length=100)
    # progress_report_type = models.CharField(max_length=5)
    # school_level = models.CharField(max_length=30)
    # peer_index = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    # grade2012 = models.CharField(max_length=1, blank=True)
    # score2012 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    # percent2012 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    # prog_score2012 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    # prog_grade2012 = models.CharField(max_length=1, blank=True)
    # perf_category2012 = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    # perf_grade2012 = models.CharField(max_length=1, blank=True)
    # environ_score = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    # environ_grade = models.CharField(max_length=1, blank=True)
    # readiness_score2012 = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    # readiness_grade2012 = models.CharField(max_length=1, blank=True)
    # additional_credit2012 = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    # prog_grade2011 = models.CharField(max_length=1, blank=True)
    # prog_grade2010 = models.CharField(max_length=1, blank=True)