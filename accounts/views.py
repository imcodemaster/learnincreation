from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy 
from django.views import View
from django.contrib.auth.forms import AuthenticationForm #add this
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#ye ha sab - forget password k ly import 
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.views.decorators.cache import cache_page


# Create your views here.




def index(request):
	return render(request, 'accounts/index.html')




def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("indexpage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="accounts/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("indexpage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="accounts/login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("indexpage")


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
       
        followers = profile.follower.all()

        for follower in followers:
        	if follower == request.user:
        		is_following = True
        		break
        	else:
        		is_following = False

        if len(followers)== 0:
        	is_following= False

        number_of_followers = len(followers)
        
        context = {
            'user': user,
            'profile': profile,
            'number_of_followers' : number_of_followers,
            'is_following':is_following,

           
        }
        return render(request, 'accounts/profile.html', context)

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = [ 'bio', 'birth_date' , "mobile" , 'standard', 'school_name' , 'academicbackground' , 'country' , 'location', 'address' , 'picture']
    template_name = 'accounts/profile_edit.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})
    
    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


#_website_setting _page
@login_required
@cache_page(60 * 15)
def setting(request):
	return render(request, 'accounts/setting.html')

#user-account-setting-page
@cache_page(60 * 15)
def accountsetting(request):
	return render(request, 'accounts/account_setting.html')


#account-securities-tips=webpage
@cache_page(60 * 15)
def secure(request):
	return render(request, 'accounts/securities.html')

class Addfollower(LoginRequiredMixin, View):
	def post(self, request, pk, *args, **kwargs):
		profile = UserProfile.objects.get(pk=pk)
		profile.follower.add(request.user)
		return redirect('profile' , pk=profile.pk)

class Removefollower(LoginRequiredMixin, View):
	def post(self, request, pk, *args, **kwargs):
		profile = UserProfile.objects.get(pk=pk)
		profile.follower.remove(request.user)
		return redirect('profile' , pk=profile.pk)



def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "accounts/password/password_reset_email.txt"
					c = {
					"email": user.email,
					'domain':'learnincreation.co.in',
					'site_name': 'Learnincreation',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'sharma.mohan57698@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("password_reset_done")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="accounts/password/password_reset.html", context={"password_reset_form":password_reset_form})