from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	mobile = forms.CharField(max_length=10,required=True)

	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email", "mobile", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.mobile = self.cleaned_data['mobile']
		if commit:
			user.save()
		return user



class ProfileForm(UserCreationForm):
	bio = forms.CharField(required=True)
	standard = forms.CharField(required=True)

	
	class Meta:
		model = UserProfile
		fields = ("bio" , "standard", "location" , "school_name")

	def save(self, commit=True):
		user = super(ProfileForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.bio = self.cleaned_data['bio']
		user.standard = self.cleaned_data['standard']
		user.school_name = self.cleaned_data['school_name']


		if commit:
			user.save()
		return user