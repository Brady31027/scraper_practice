# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.views.decorators.csrf import ensure_csrf_cookie
from time import gmtime, strftime

@ensure_csrf_cookie
def index(request):
	contents = ""
	valid = -1
	if request.method == 'POST':
		try:
			contents = request.POST['contents']
			if len(contents.strip()) == 0:
				contents = ""
				valid = 0
				pass
			else:
				ip = request.POST['ip']
				city = request.POST['city']
				state = request.POST['state']
				country = request.POST['country']
				time = strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' Pacific Time (UTC-8)'
				valid = 1
		except:
			contents = ""
			valid = 0
			pass
		
	return render(request, 'index.html', locals())