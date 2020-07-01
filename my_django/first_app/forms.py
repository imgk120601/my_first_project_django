#this is created manually by me creating a class FormName
from django import forms
from django.forms import ModelForm

from django.core import validators
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo

class UserForm(forms.ModelForm):      #thsi is must in forms.ModelForm 
	password=forms.CharField(widget=forms.PasswordInput)#we have added password field in user's built-in field

	class Meta():      #use meta class in forms.ModelForm
		model=User 		#use model=User  and use in-built fields of User
		fields=('username','email','password')

class UserProfileInfoForm(forms.ModelForm):       #this is using models.py's class
	#already in herited
	class Meta():                      #in this use model='classname'(in models.py)
		model=UserProfileInfo			#field=('extra field created by us in')
		fields=('portfolio_site','profile_pic')

'''def my_own_validator(value): #creating my own validator and here term --value-- help django to recognise it as validator
	if value[0].isupper()==False:
		raise forms.ValidationError('ValidationError hai bhai!! Are bhai phla word in Name should be in capital')

class FormName(forms.Form):
	name=forms.CharField(validators=[my_own_validator])#we are using our self_made validator in name field
	email=forms.EmailField()
	verify_email=forms.EmailField(label='Enter your email again')#we are verifying the email #label is just the name appear left to email input box
	text=forms.CharField(widget=forms.Textarea)
	bot_catcher=forms.CharField( required=False ,widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)]) # this validator only bot_catcher#try to find the bot who want to log in into your website----required=False---

	def clean(self):
		all_data_clean=super().clean()
		email=all_data_clean['email']
		verify_email=all_data_clean['verify_email']

		if email!=verify_email:
			raise forms.ValidationError('ValidationError hai bhai!! Email verification failed Please verify email correctly.')'''


