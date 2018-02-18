from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View 

import json
from braces.views import CsrfExemptMixin
from django.views.decorators.csrf import csrf_exempt

from twilio.twiml.messaging_response import MessagingResponse

def index(request):
	return HttpResponse('<h1>ParticleHooks</h1>')

@csrf_exempt
def sms_response(request):
	resp = MessagingResponse()
	msg = resp.message("Check out this sweet owl!")
	msg.media("https://demo.twilio.com/owl.png")
	return HttpResponse(str(resp))


class ProcessHookView(CsrfExemptMixin, View):

	def post(self, request, *args, **kwargs):
		print(json.loads(request.body))
		return HttpResponse()