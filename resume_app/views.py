from django.shortcuts import render, redirect
from tika import parser

from .forms import *
from django.http import JsonResponse
from django.http import StreamingHttpResponse
from django.http import HttpResponseRedirect
import json
from .code1 import *

import pprint
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import requests
from subprocess import run,PIPE
import sys



def basic(request):
	return render(request,'basic.html')

def basic_info(request):
	return render(request,'basic_info.html')

def select_post(request):	
	return render(request,'select_post.html')

def index(request):
	return render(request, 'index.html')

def login(request):
	return render(request, 'login.html')

def login_admin(request):
		return render(request, 'login_admin.html')       
           
def candidate(request):
	return render(request, 'candidate.html')

def reception(request):
	return render(request, 'reception.html')


def upload_cv(request):
	submitted = False
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save() 
	else:
		form = DocumentForm()
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'upload_cv.html', {'form': form,'submitted': submitted})

def technical_info(request):
	if request.method == "POST":
		form = technicalForm(request.POST)
		if form.is_valid():
			form.save()
	else:	
		print(doc_url)
		datas=motherFunc(doc_url)
		print(datas)
		joined_skill=', '.join(datas[1])	
		marks10=datas[0]['secondary']
		marks12=datas[0]['sr.secondary']
		ugperc=datas[0]['bachelors'].split(',')
		pgperc=datas[0]['masters'].split(',')
		interest=datas[2]['INTEREST']
		intFormatted=', '.join(interest)
		phd=datas[0]['phd']
		print(marks10)
				
		data = {
			'perc_10':marks10,
			'perc_12':marks12,
			'perc_ug':ugperc[0],
			'ug_degree':ugperc[1],
			'pg_perc':pgperc[0],
			'pg_degree':pgperc[1],
			'skill_set':joined_skill,
			'phd_spec':phd,
			'interest':intFormatted
			}


		form = technicalForm(initial=data)
	return render(request,'technical_info.html',{'form':form})

def success(request):
	return render(request, 'success.html')

def login_admin(request):
	return render(request, 'login_admin.html')

def postreq(request):
	json_data = json.loads(request.body)
	print("Datastream from front: begin............")
	pprint.pprint(json_data)
	global doc_url
	doc_url=json_data['doc_url']
	print("Datastream from front: end............")
	newDum = candidate_info(name = json_data['name'],phno = json_data['phno'],email = json_data['email'],dob = json_data['dob'], gender = json_data['gender'],Add1 = json_data['Add1'],Add2 = json_data['Add2'],city = json_data['city'],state = json_data['state'],pin = json_data['pin'],pType = json_data['pType'],desig=json_data['desig'],dept = json_data['dept'])
	newDum.save()
	return JsonResponse(json_data)

def test(request):
	return render(request,'test.html')

def output(request):
	data = requests.get("https://reqres.in/api/users")
	print("This is data:",data.text)
	data = data.text
	return render(request,'test.html',{'data':data})

def external(request):
	hello="THIS IS INSIDE EXTERNAL"
	skill_set = extract_skill(info['SKILL'])
	edu = extract_education(info['EDUCATION'])
	return render(request,'test.html',{'data2':skill_set[0],'data3':'EDUCATION: ','data4':edu,'data5':info})

def url(request):
	json_data=json.loads(request.body)
	allvideos= Document.objects.all()
	context= {'allvideos': allvideos}

