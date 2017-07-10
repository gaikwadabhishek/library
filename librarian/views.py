
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf.urls import include
from django.template import loader
from .models import Librarian
from django.http import Http404
from .forms import SignUpForm,AddBookForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# Create your views here.

@login_required
def home(request):
    return render(request, 'home1.html')

def signup_success(request):
    return render(request,'signup_success1.html')

def add_book(request):
    return render(request,'add_book.html')
    
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.librarian.librarian_name = form.cleaned_data.get('librarian_name')
			user.librarian.email = form.cleaned_data.get('email')
			user.librarian.phone_number = form.cleaned_data.get('phone_number')
			user.refresh_from_db()
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('signup_success1')
	else:
		form = SignUpForm()
	return render(request, 'signup1.html', {'form': form})

def add_book(request):
	form = AddBookForm()
	if request.method=='POST':
		form = AddBookForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			
			

			
	return render(request,'add_book.html',{'form':form})




"""	title = forms.CharField(required=True,help_text='Enter title of the book')
	author = forms.CharField(required=True,help_text='Enter author of the book')
	publication = forms.CharField(required=True,help_text='Enter publication of the book')
	unique_id = forms.CharField(required=True,help_text='Enter unique id of the book')
	"""
