from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views as student_views
urlpatterns =[

	url(r'^$', student_views.home, name ='home'),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
	url(r'^signup/$', student_views.signup, name='signup'),
	url(r'^signup_success/$', student_views.signup_success, name ='signup_success'),
]
