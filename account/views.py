from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

def join_view(request):

	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		return render(request, 'join.djhtml')

@csrf_exempt
def join_ok(request):

	if request.method == "POST":
		try:
			id = request.POST['id']
			password = request.POST['password']
			email = request.POST['email']

		except:
			pass

	else:
		return HttpResponseRedirect('/')