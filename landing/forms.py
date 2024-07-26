from django import forms
from .models import *

class ThinkForm(forms.ModelForm):
	class Meta:
		model = Think
		fields = ['title' , 'author']

