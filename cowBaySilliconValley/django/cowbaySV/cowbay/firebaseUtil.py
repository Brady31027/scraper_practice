# -*- coding: UTF-8 -*-
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
		jsonData = json.dumps(hashData)
		result = fb.post("/posts", jsonData)
		return result['name']