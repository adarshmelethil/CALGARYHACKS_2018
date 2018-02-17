from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View 

import json
from braces.views import CsrfExemptMixin


def index(request):
	return HttpResponse('<h1>ParticleHooks</h1>')


class ProcessHookView(CsrfExemptMixin, View):

	def post(self, request, *args, **kwargs):
		print(json.loads(request.body))
		return HttpResponse()