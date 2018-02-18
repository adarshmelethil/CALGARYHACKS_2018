from django.http import HttpResponse

from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View 
from .forms import UserForm
from braces.views import CsrfExemptMixin

# Create your views here.


class MainPage(CsrfExemptMixin, View):
	form_class = UserForm
	template_name = 'main/index.html'

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		form = request.POST
		my_form = form.dict()
		if 'usernamesignup' in my_form:
			username = form['usernamesignup']
			password = form['passwordsignup']
			if not User.objects.filter(username=username).exists():
				user = User.objects.create_user(username, password)
				user.set_password(password)
				user.save()
		elif 'username' in my_form:
			username = form['username']
			password = form['password']

		user = authenticate(username=username, password=password)
		print(user)
		# print('Authenticating: ', user)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('ParticleHooks:profile')

		return render(request, self.template_name)
# def index(request):

# 	return render(request, 'main/index.html',{})

