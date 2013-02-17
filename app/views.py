from django.http import HttpResponse
from django.shortcuts import render
import os, traceback, sys
from app.models import Event, School, Teacher, Graduation, Demographic, Final
from django.core import serializers
import requests, json
from django.views.decorators.csrf import csrf_exempt
import csv
from csv import reader
from django.shortcuts import redirect
import bitly_api
from embedly import Embedly

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


def filter_from_bitly(bitly_link, bitly_connection, category):
	c = bitly_connection
	if category in c.link_category(bitly_link):
		return True
	else:
		return False

def search_from_bitly(query, token, category='Education'):
	c = bitly_api.Connection(access_token=token)
	retrieved = c.search(query)
	results = list()
	for link in retrieved:
		if filter_from_bitly(link['aggregate_link'],c, category):
			results.append(link['aggregate_link']) 
	return results


def get_list_from_embedly(bitly_url_links,KEY):
	client = Embedly(KEY)
	data_dict = dict()
	temp_dict = dict()
	for p,link in enumerate(bitly_url_links):
		link = client.oembed(link)
		temp_dict['title'] = link['title']
		temp_dict['url'] = link['url']
		temp_dict['thumbnail_url'] = link['thumbnail_url']
		temp_dict['thumbnail_width'] = link['thumbnail_width']
		temp_dict['description'] = link['description']
		data_dict[p] = temp_dict
	return data_dict

@csrf_exempt 
def home(request, dbn=None, teacher_id=None):

	school = None
	teacher = None
	demographic = None
	graduation = None

	if request.method == 'POST':
		s_list = School.objects.filter(dbn=request.POST['school'])
		if s_list:
			school = s_list[0]
			dbn = school.dbn
			return redirect('/home/%s' % dbn)

	schools = School.objects.all()
	teachers = []
	if dbn:
		teachers = Teacher.objects.filter(dbn=dbn).order_by('teacher_name_first_1').distinct('teacher_name_first_1').all()
		s_list = School.objects.filter(dbn=dbn)
		if s_list:
			school = s_list[0]
		d_list = Demographic.objects.filter(dbn=dbn)
		if d_list:
			demographic = d_list[0]
		g = Graduation.objects.filter(dbn=dbn)
		if g:
			graduation = g[0]


	if teacher_id:
		teacher = Teacher.objects.filter(teacher_id=teacher_id)[0]

	s = {'teachers': teachers,
    	'schools': schools}

	if school:
		s['school'] = school

	if teacher:
		s['teacher'] = teacher

	if dbn:
		s['dbn'] = dbn

	if demographic:
		s['demographic'] = demographic

	if graduation:
		s['graduation'] = graduation

	# query = "ny teacher"
	# TOKEN = "75cd1829b1d41b592520c62617803adb19f1d8f5"
	# results = search_from_bitly(query, TOKEN)
	# KEY = '370a46d4db464e15abf6a21fbc33224c'
	# data_dict = get_list_from_embedly(results, KEY)

	# print data_dict

	# s['thumb1'] = data_dict[0]['thumbnail_url']
	# s['thumb2'] = data_dict[1]['thumbnail_url']

	# for num in data_dict.keys():
	# 	data = data_dict[num]
	# 	s['thumb1'] = data['thumbnail_url']

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
	# with open('data/schools.csv', 'rb') as csvfile:
	# 	csvreader = csv.reader(csvfile)
	# 	i = -1
	# 	for cols in csvreader:
	# 		i+=1
	# 		if i in (0,1,2):
	# 			continue
	# 		cols = cols[1:]
	# 		for i, col in enumerate(cols):
	# 			cols[i] = (col or 0)
	# 		try:
	# 			s = School(
	# 				dbn=cols[0][:10],
	# 				district=cols[1][:2],
	# 				name=cols[2][:100],
	# 				principal=cols[3][:100],
	# 				progress_report_type=cols[4][:5],
	# 				school_level=cols[5][:30],
	# 				peer_index=float(cols[6] or 0),
	# 				grade2012=cols[7][:1],
	# 				score2012=cols[8],
	# 				percent2012=cols[9],
	# 				prog_score2012=cols[10],
	# 				prog_grade2012=cols[11],
	# 				perf_category2012=cols[12],
	# 				perf_grade2012=cols[13],
	# 				environ_score=cols[14],
	# 				environ_grade=cols[15],
	# 				readiness_score2012=cols[16],
	# 				readiness_grade2012=cols[17],
	# 				additional_credit2012=cols[18],
	# 				prog_grade2011=cols[19],
	# 				prog_grade2010=cols[20])
	# 			s.save()
	# 		except:
	# 			print cols
	# 			print traceback.print_exc(file=sys.stdout)


	# Teacher.objects.all().delete()
	# csvfile = open('data/teachers_matched.csv', 'rb')
	# csvreader = csv.reader(csvfile)
	# i = -1
	# for cols in csvreader:
	# 	i+=1
	# 	if i in [0]:
	# 		continue
	# 	cols = cols[1:]
	# 	for i, col in enumerate(cols):
	# 		cols[i] = (col or 0)
	# 	t = Teacher()
	# 	t.teacher_name_first_1 = ''.join([c for c in cols[0] if c != '"'])
	# 	t.teacher_name_last_1 = ''.join([c for c in cols[1] if c != '"'])
	# 	if cols[2] != 'NA':
	# 		t.teacher_id = cols[2]
	# 	t.dbn = ''.join([c for c in cols[-10] if c != '"'])
	# 	t.grade0708 = cols[4]
	# 	t.grade0809 = cols[5]
	# 	t.grade0910 = cols[6]
	# 	t.va_0506 = clean_num(cols[-16])
	# 	t.va_0607 = clean_num(cols[-15])
	# 	t.va_0708 = clean_num(cols[-14])
	# 	t.va_0809 = clean_num(cols[-13])
	# 	t.va_0910 = clean_num(cols[-12])
	# 	s_list = School.objects.filter(dbn=t.dbn)
	# 	if s_list:
	# 		t.school = s_list[0]
	# 	try:
	# 		t.save()
	# 	except:
	# 		print traceback.print_exc(file=sys.stdout)

	# Graduation.objects.all().delete()
	# csvfile = open('data/grads.csv', 'rb')
	# csvreader = csv.reader(csvfile)
	# i = -1
	# for cols in csvreader:
	# 	i+=1
	# 	for i, col in enumerate(cols):
	# 		cols[i] = (col or 0)
	# 		if col == 's':
	# 			cols[i] = 0
	# 		if '%' in str(col):
	# 			cols[i] = col.replace('%', '')
	# 	g = Graduation()
	# 	g.dbn = ''.join([c for c in cols[0][:10] if c != '"'])
	# 	g.name = cols[1]
	# 	g.year = cols[2]
	# 	if '%' in str(cols[6]):
	# 		cols[6] = cols[6].replace('%','')
	# 	g.grads_percent = cols[6]
	# 	g.regents_num = cols[7]
	# 	g.regents_percent_total = cols[8]
	# 	g.regents_percent_grad = cols[9]
	# 	g.advregents_percent_grad = cols[12]
	# 	g.othregents_percent_grad = cols[15]
	# 	g.local_percent_grad = cols[18]
	# 	g.drop_percent = cols[-1]
	# 	s_list = School.objects.filter(dbn=g.dbn)
	# 	if s_list:
	# 		g.school = s_list[0]

	# 	g.drop_percent = cols[-1]

	# 	e_g = Graduation.objects.filter(dbn=g.dbn)
	# 	if not e_g:			
	# 		try:
	# 			g.save()
	# 		except:
	# 			print cols
	# 			print traceback.print_exc(file=sys.stdout)

	# Demographic.objects.all().delete()
	# csvfile = open('data/demo.csv', 'rb')
	# csvreader = csv.reader(csvfile)
	# i = -1
	# for cols in csvreader:
	# 	i+=1
	# 	if i in [0]:
	# 		continue
	# 	for i, col in enumerate(cols):
	# 		cols[i] = (col or 0)
	# 	d = Demographic()
	# 	d.dbn = ''.join([c for c in cols[0][:10] if c != '"'])
	# 	d.name = cols[1]
	# 	d.year = cols[2]
	# 	d.freelunch_reduced_percent = float(cols[4] or 0)
	# 	d.asian_percent = cols[7]
	# 	d.black_percent = cols[8]
	# 	d.hispanic_percent = cols[9]
	# 	d.white_percent = cols[10]
	# 	try:
	# 		d.save()
	# 	except:
	# 		print cols
	# 		print traceback.print_exc(file=sys.stdout)

	csvfile = open('data/final.csv', 'rb')
	csvreader = csv.reader(csvfile)
	i = -1
	for cols in csvreader:
		i+=1
		if i in [0]:
			continue
		for i, col in enumerate(cols):
			cols[i] = (col or 0)
		dbn = ''.join([c for c in cols[0][:10] if c != '"'])
		s = School.objects.filter(dbn=dbn)
		if s:
			school = s[0]
			if not school.grade2012:
				school.grade2012 = cols[-2]
				school.save()
		# if not s:
		# 	school = School(
		# 		dbn=dbn,
		# 		name=cols[9])
		# 	school.save()
		# d = Demographic.objects.filter(dbn=dbn)
		# if not d:
		# 	demographic = Demographic(
		# 		dbn=dbn,
		# 		freelunch_reduced_percent=cols[14])
		# 	demographic.save()
		# t = Teacher.objects.filter(dbn=dbn)
		# if t:
		# 	teacher = t[0]
		# 	if teacher.va_0607 in [0, None]:
		# 		teacher.va_0607 = cols[8]
		# 	if teacher.va_0708 in [0, None]:
		# 		teacher.va_0708 = cols[6]
		# 	if teacher.va_0809 in [0, None]:
		# 		teacher.va_0809 = cols[4]
		# 	if teacher.va_0910 in [0, None]:
		# 		teacher.va_0910 = cols[2]
		# 	teacher.save()

	return render(
    	request,
    	'index.html')

def clean_num(s):
	if s in ('NA', 'NA\n', '', None):
		return 0
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