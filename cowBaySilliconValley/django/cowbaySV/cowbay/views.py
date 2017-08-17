# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.views.decorators.csrf import ensure_csrf_cookie
from time import gmtime, strftime
from firebase import firebase
import requests
import json
import sys
import time

class FirebaseUtil:
	def __init__(self, article, ip, city, state, country, time):
		self.url = 'https://cowbaysillionvalleybradycheng.firebaseio.com/'
		self.ip = ip
		self.article = article
		self.city = city
		self.state = state
		self.country = country
		self.time = time

	def post(self):
		fb = firebase.FirebaseApplication(self.url, None)
		hashData = {'article': self.article,
					'ip': self.ip,
					'city': self.city,
					'state': self.state,
					'country': self.country,
					'time': self.time
		}
		try:
			jsonData = json.dumps(hashData)
			result = fb.post("/posts", jsonData)
			return result['name']
		except:
			return -1

def saveToDB(contents, ip, city, state, country, time):
	db = FirebaseUtil(contents, ip, city, state, country, time)
	key = db.post()
	if key == -1: # error happened while posting
		return -1
	return 1

@ensure_csrf_cookie
def index(request):
	contents = ""
	valid = 100
	if request.method == 'POST':
		try:
			contents = request.POST['contents']
			if len(contents.strip()) == 0:
				contents = ""
				valid = 0
			else:
				ip = request.POST['ip']
				city = request.POST['city']
				state = request.POST['state']
				country = request.POST['country']
				time = strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' Pacific Time (UTC-8)'
				valid = saveToDB(contents, ip, city, state, country, time)
				if valid == 1:
					print('redirect')
					return HttpResponseRedirect('posting')
				else:
					print('cannot redirect')
			
		except:
			contents = ""
			valid = 0
	return render(request, 'index.html', locals())

def posting(request):
	return render(request, 'posting.html', locals())		
	