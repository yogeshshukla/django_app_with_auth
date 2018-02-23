from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django import forms
from django.template import loader
from django.urls import reverse
from django.conf import settings
from django.shortcuts import redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import User

# Create your views here.
def register(request):
	if request.method == 'POST':
	    form = UserRegistrationForm(request.POST)
	    if form.is_valid():
	        userObj = form.cleaned_data
	        username = userObj['username']
	        email =  userObj['email']
	        password =  userObj['password']
	        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
	            User.objects.create_user(username, email, password)
	            user = authenticate(username = username, password = password)
	            login(request, user)
	            return HttpResponseRedirect('/polls')
	        else:
	        	return render(request, 'registration/register.html', {'error_message' : 'Looks like a username with that email or password already exists', 'form' : form})
	else:
	    form = UserRegistrationForm()
	return render(request, 'registration/register.html', {'form' : form})
