#this is created manually by me creating a class FormName
from django import forms

class FormName(forms.Form):
	name=forms.CharField()
	email=forms.EmailField()
	text=forms.CharField(widget=forms.Textarea)
