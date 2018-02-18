
import os

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import View 

import json
from braces.views import CsrfExemptMixin
from twilio.rest import Client 
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test

from .models import Devices, PhoneNumber

def is_user_active(user):
    return user.is_active

@user_passes_test(is_user_active, login_url='/')
def profile(request):
	return render(request, 'ParticleHooks/profile.html', {})

@user_passes_test(is_user_active, login_url='/')
def addDevice(request):
	post = request.POST
	device = Devices(user=request.user)
	device.coreid = post['coreid']
	device.save()
	print('add d:', request.POST)
	return redirect('ParticleHooks:profile')

@user_passes_test(is_user_active, login_url='/')
def removeDevice(request):
	post = request.POST
	Devices.objects.filter(id=int(post['deviceid'])).delete()
	print('remove d:', request.POST)
	return redirect('ParticleHooks:profile')

@user_passes_test(is_user_active, login_url='/')
def addNumber(request):
	post = request.POST
	num = PhoneNumber(user=request.user)
	num.phone_num = post['numberid']
	num.save()
	print('add n:', request.POST)
	return redirect('ParticleHooks:profile')

@user_passes_test(is_user_active, login_url='/')
def removeNumber(request):
	post = request.POST
	PhoneNumber.objects.filter(id=int(post['numberid'])).delete()
	print('remove n:', post['numberid'])
	return redirect('ParticleHooks:profile')

@user_passes_test(is_user_active, login_url='/')
def logoutuser(request):
	logout(request) 
	return redirect('main:index')

class ProcessHookView(CsrfExemptMixin, View):

	def sendSMSMessage(self, msg, to):
		account_sid = 'AC19460052ec76211b5ea9a719ee78bbed'
		auth_token = '27dd45ac6bf1123da30daccce8746475'
		from_num = '+15873551468'

		client = Client(account_sid, auth_token)

		message = client.messages.create(
			to,
			from_=from_num,
			body=msg
			)

		return message 

	def processJSON(self, json_msg, to):
		if 'sms' in json_msg:
			self.sendSMSMessage(json_msg['sms'], to)

	def post(self, request, *args, **kwargs):
		# print("RAW: ", request.body)
		info = json.loads(request.body)
		# print("JSON: ", info)
		data = info['data']
		
		if type(data) is str:
			data = json.loads(data)

		# print("data: '"+ data+"'")
		print("data: ", data)
		# print("keys:", data.keys())
		msg = self.processJSON(data, '+14038605837')
		print("Message: ", msg)
		# data = json.loads(info['data'])
		# print("data: ", data)


		return HttpResponse()