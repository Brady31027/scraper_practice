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
		data = {'article': self.article,
				'ip': self.ip,
				'city': self.city,
				'state': self.state,
				'country': self.country,
				'time': self.time
		}
		try:
			result = fb.post("/posts", json.dumps(data))
			return result['name']
		except:
			return -1

def saveToDB(contents, ip, city, state, country, time):
	db = FirebaseUtil(contents, ip, city, state, country, time)
	key = db.post()
	if key == -1: # error happened while posting
		return -1
	return 1

def sendMail(tags, reasons, ip, city, state, country, time):
	print('[Mail] ', tags, ' ', reasons)
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
					return HttpResponseRedirect('posting')
		except:
			contents = ""
			valid = 0
	return render(request, 'index.html', locals())

def posting(request):
	msg_doing = "貼文儲存中"
	msg_done = "成功存入資料庫，等待張貼，即將跳轉首頁"
	return render(request, 'posting.html', locals())

def feedback(request):
	tags, reasons, valid = "", "", 100
	if request.method == 'POST':
		try:
			tags = request.POST['tags']
			reasons = request.POST['reasons']
			if len(tags.strip()) == 0 or len(reasons.strip()) == 0:
				tags, reasons = "", ""
				print("err1")
				valid = 0
			else:
				ip = request.POST['ip']
				city = request.POST['city']
				state = request.POST['state']
				country = request.POST['country']
				time = strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' Pacific Time (UTC-8)'
				valid = sendMail(tags, reasons, ip, city, state, country, time)
				if valid == 1:
					return HttpResponseRedirect('feedbacking')	
				print("err2")
		except:
			print("err3")
			tags, reasons, valid = "", "", 0
	return render(request, 'feedback.html', locals())

def feedbacking(request):
	msg_doing = "訊息發送中"
	msg_done = "訊息已發送，即將跳轉首頁"
	return render(request, 'posting.html', locals())


	