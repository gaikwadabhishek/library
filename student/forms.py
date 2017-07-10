from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from phonenumber_field.modelfields import PhoneNumberField
class SignUpForm(UserCreationForm):
	student_name = forms.CharField(max_length=50, help_text='Enter your full name')
	email = forms.EmailField(max_length=254,  required=True, help_text='Inform a valid email address.')
	#phone_number = PhoneNumberField(max_length=13,  required=True, help_text='Enter your phone number')
	phone_number = forms.CharField(max_length=15,  required=True, help_text='Enter your phone number')
	class Meta:
		model = User
		fields = ('username', 'student_name' , 'email', 'phone_number', 'password1', 'password2', )
		widgets = {
			'username': forms.TextInput(),
			'student_name':forms.TextInput(),
			'email':forms.TextInput(),
			'phone_number':forms.TextInput(),
			'password1':forms.TextInput(),
			'password2':forms.TextInput()
		}
