from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf.urls import include
from django.template import loader
from .models import Student
from django.http import Http404
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

def signup_success(request):
    return render(request,'signup_success.html')
    
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.student.student_name = form.cleaned_data.get('student_name')
			user.student.email = form.cleaned_data.get('email')
			user.student.phone_number = form.cleaned_data.get('phone_number')
			user.refresh_from_db()
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('signup_success')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})
