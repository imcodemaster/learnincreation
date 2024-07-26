'''
Learnincreation and Learnincreation geeks run on same domain , learnincreation .co.in
to move in learnincreation login not required , 
however, learnincreation geeks required login details
dynamic e-learning portal
root path - shows search bar - no login need 
show search result 
wanna particular post id access , login required !! _ WELCOME TO LEARNING WORLD 

rest , learnincreation - home, about , product, founder desk (later version update),
contact , notice section (later version update)  (with tooltip)

geeks - include my squad 
geeks detail on geeks app -- 

language detail - new version update

'''
 
#import section ---- 
from django.shortcuts import render
from landing.models import Contact, Think, Subscribe , doodle
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView , ListView, DetailView, CreateView,UpdateView,DeleteView # importing class based views from views.generic
from django.core.paginator import Paginator
from django.urls import reverse_lazy , reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from geeks.models import *
from django.views.decorators.cache import cache_page
from django.http import HttpResponseRedirect
# Create your views here.  

#doodle_explore_section

class doodlelistView(ListView):
	model = doodle
	template_name = 'landing/doodle_list.html' #<app>/<model>_<viewtype>.html
	context_objects_name = 'doodle'
	ordering = ['-date']
	paginate_by = 10 # pagination  (django provided )




class doodlelistDetailView(LoginRequiredMixin,DetailView):
    model = doodle
    template_name = 'landing/doodle_detail.html' #<app>/<model>_<viewtype>.html
    
    def get_context_data(self , *args , **kwargs):
        stuff = get_object_or_404(doodle, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        got_liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            got_liked = True

        context = super(doodlelistDetailView , self).get_context_data( *args , **kwargs)
        context ['objects_name'] = 'doodle'
        context ['total_likes'] = total_likes
        context ['got_liked'] = got_liked
        return context
 

#__doodle_creation_updation-deletion 


class doodleCreateView(LoginRequiredMixin, CreateView):
    model = doodle #describing models 
    fields = [ 'event', 'tooltip', 'detail' , 'moredetail','img' ] #describe the field need to create 
    success_url = reverse_lazy('doodle-list')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class doodleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView,):
    model = doodle
    fields = [ 'event' , 'tooltip' , 'detail' , 'moredetail' , 'img'  ] #describe the field need to Update
    success_url = reverse_lazy('doodle-list')
    
    def form_valid(self,form):

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):

        doodle = self.get_object()

        if self.request.user == doodle.author:
            return True
        return False 

class doodleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView,):
    model = doodle
    success_url = reverse_lazy('doodle-list')

    def test_func(self):
        doodle = self.get_object()
        if self.request.user == doodle.author:
            return True
        return False 




def doodleLikeView(request , pk):
    post = get_object_or_404(doodle, id=request.POST.get('doodle_id'))
    got_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        got_liked = False
    else:
        post.likes.add(request.user)
        got_liked = True
    return HttpResponseRedirect(reverse('doodle-detail' , args=[str(pk)]))



#welcome

def index(request):
	return render(request, 'landing/index.html')




#_website_home_view
@cache_page(60 * 15)
def home(request):
    return render(request, 'landing/home.html') 

#search lesson view  (coursse lesson)
class SearchResultsListView(ListView): # turns to announcment
    model = CourseArticle
    template_name = 'landing/search_results.html' #<app>/<model>_<viewtype>.html

    def get_queryset(self):
    	query = self.request.GET.get("q")
    	object_list = CourseArticle.objects.filter(
    		Q(tags__icontains=query) | Q(title__icontains=query) | Q(body__icontains=query)
    		)
    	return object_list 

#think with learnincreation thought section view (notice)

class ThinkListView(ListView): # turns to announcment
    model = Think
    template_name = 'landing/think_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'think'
    ordering = ['-published']
    paginate_by = 10 # pagination  (django provided )


#_website_about _page
@cache_page(60 * 15)
def about(request):
	return render(request, 'landing/about.html')


#product
@cache_page(60 * 15)
def product(request):
	return render(request, 'landing/product.html')

'''
#faculty view - front end 

def faculty(request):
    teacher = Teacher.objects.all()
    context = {'teacher':teacher}
    return render(request, 'landing/faculty.html',context)

#our pride section - front end - for student 

def encouragement(request):
    pride = Pride.objects.all()
    context = {'pride':pride}
    return render(request, 'info/ourpride.html',context)

'''

'''
#campus_details For frontend 

def campus(request):
    return render(request, 'info/ourcampus.html' , context)

def our_department(request):
    department_dynamic = Department.objects.all()
    context = {'department_dynamic':department_dynamic}
    return render(request, 'info/our_department.html' , context)


'''

#contact view for website 

class ContactView(CreateView):
	model = Contact
	fields = ['first_name', 'second_name' , 'to_the_department',  'email' , 'mobile' , 'message' ] #describe the field need to create 
	success_url = reverse_lazy('home')


#gallary ection dynamic view - 
@cache_page(60 * 15)
def gallary(request):
	return render(request, 'landing/gallary.html')

#becybersmartcampign
def cybersmart(request):
	return render(request, 'landing/cybersmart.html')




#subscribe view

class SubscribeView(CreateView):
	model = Subscribe
	fields = ['first_name', 'second_name' , 'Subscription' ,  'institute' , 'course' , 'registration_number' , 'email' , 'mobile' ] #describe the field need to create 
	success_url = reverse_lazy('home')



#_website_pricing and payment _page
@cache_page(60 * 15)
def paymentpage(request):
	return render(request, 'landing/payment.html')



# share your knowledge
#@cache_page(60 * 15)
def shareyourknowledge(request):
	return render(request, 'landing/campaign.html')




#_website_FAQ _page
@cache_page(60 * 15)
def faq(request):
	return render(request, 'landing/faq.html')


# learnincreation for business
@cache_page(60 * 15)
def business(request):
	return render(request, 'landing/business.html')



# policies

def policies(request):
	return render(request, 'landing/policies.html')

#_website_terms_page

def terms(request):
	return render(request, 'landing/terms.html')



#_website_terms_page

def community(request):
	return render(request, 'landing/community.html')



# learnincreatoin pictures

def picture(request):
	return render(request, 'landing/learnincreationpicture.html')

#_website_helpdesk _page
@cache_page(60 * 15)
def helpdesk(request):
	return render(request, 'landing/helpdesk.html')

'''
# geeks-blog-article-list
class businessprofileView(ListView): # turns to announcment
    model = businessProfile
    template_name = 'landing/businessprofile_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'shop'
    ordering = ['-date']
  

class businessprofileCreateView(LoginRequiredMixin, CreateView):
	model = businessProfile
	fields = ['business_name', 'mobile'   , 'snap' , 'email', 'description' , 'sector' , 'location' ] #describe the field need to create 
	success_url = reverse_lazy('business')


# geeks-courses-detail
class businessprofileDetailView(LoginRequiredMixin, DetailView):
	model = businessProfile
	template_name = 'landing/business_detail.html'


class businessprofileUpdateView(LoginRequiredMixin, UpdateView):
	model = businessProfile
	fields = ['business_name', 'mobile'   , 'snap' , 'email', 'description' , 'sector' , 'location' ] #describe the field need to create
	template_name = 'landing/businessprofile_update.html'
	success_url = reverse_lazy('business')


class businessprofileDeleteView(LoginRequiredMixin, DeleteView):
	model = businessProfile
	success_url = reverse_lazy('business')

'''

