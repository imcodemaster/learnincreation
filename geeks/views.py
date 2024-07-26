from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import View, ListView, CreateView,  DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from django.urls import reverse_lazy 
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.views.decorators.cache import cache_page
from .render import Render
# Create your views here.

# geeks-portal-home
@cache_page(60 * 15)
def geeks_home(request):
	return render(request, 'geeks/geeks_home.html')


#_website_pathway _page

def pathway(request):
	return render(request, 'geeks/pathway.html')





class lessonpdfView(DetailView):

    def get(self, request):
        quicklearn = Quicklearn.objects.all()
        today = timezone.now()
    
        params = {
            'today': today,
            'quicklearn': quicklearn,
            'request': request
            }
        return Render.render( '../templates/geeks/lesson_pdf.html',  params)    




#courselesson
class courselessonpdfView(DetailView):

    def get(self, request):
        lesson = CourseArticle.objects.all().filter(lessonbookmark=request.user)
        today = timezone.now()
    
        params = {
            'today': today,
            'lesson': lesson,
            'request': request
            }
        return Render.render( '../templates/geeks/courselesson_pdf.html',  params)    



# geeks-course-list

class CourseListView(ListView): # turns to announcment
    model = Course
    template_name = 'geeks/course_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'course'
    ordering = ['-published_on']
  

class CourseCreateView(LoginRequiredMixin, CreateView):
	model = Course
	fields = ['name',  'standard' , 'description' , 'detail' , 'tags' , 'meta' , 'snap' , 'videofile'] #describe the field need to create 
	success_url = reverse_lazy('geeks-courses')


# geeks-courses-detail

class CourseDetailView(DetailView):
	model = Course
	template_name = 'geeks/course_detail.html'


class CourseUpdateView(LoginRequiredMixin, UpdateView):
	model = Course
	fields = ['name' ,'standard' , 'description' , 'detail' , 'tags' ,  'meta', 'snap' , 'videofile'] #describe the field need to create 
	template_name = 'geeks/course_update.html'
	success_url = reverse_lazy('geeks-courses')


class CourseDeleteView(LoginRequiredMixin, DeleteView):
	model = Course
	success_url = reverse_lazy('geeks-courses')

def category(request , cat_id):
	category_lesson = CourseArticle.objects.filter(course = cat_id)
	return render(request, 'geeks/category_list.html' , {'cat_id':cat_id , 'category_lesson':category_lesson})

# course-article-views 
# geeks-course-list

class CoursearticleListView(ListView): # turns to announcment
    model = CourseArticle
    template_name = 'geeks/coursearticle_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'lesson'
    ordering = ['-published_on']



class CoursearticleCreateView(LoginRequiredMixin, CreateView):
	model = CourseArticle
	fields = ['course', 'standard' , 'meta' ,'title' , 'keynote' , 'tags'   , 'snap' , 'body', 'heading_add_1' , 'snap_add_1' , 'body_add_1'
	, 'heading_add_2' ,  'snap_add_2' , 'body_add_2', 'heading_add_3' , 'snap_add_3' , 'body_add_3', 'heading_add_4' ,  'snap_add_4' , 'body_add_4', 'heading_add_5' , 'snap_add_5' , 'body_add_5', 'heading_add_6' ,  'snap_add_6' , 'body_add_6', 'heading_add_7' , 'body_add_7'] #describe the field need to create 
	success_url = reverse_lazy('geeks-coursearticle')


# geeks-courses-detail

class CoursearticleDetailView(LoginRequiredMixin, DetailView):
	model = CourseArticle
	template_name = 'geeks/coursearticle_detail.html'


class CoursearticleUpdateView(LoginRequiredMixin, UpdateView):
	model = CourseArticle
	fields = ['course', 'standard' , 'meta' , 'title' , 'keynote' , 'tags'   , 'snap' , 'body', 'heading_add_1' , 'snap_add_1' , 'body_add_1'
	, 'heading_add_2' ,  'snap_add_2' , 'body_add_2', 'heading_add_3' , 'snap_add_3' , 'body_add_3', 'heading_add_4' , 'snap_add_4' , 'body_add_4', 'heading_add_5' , 'snap_add_5' , 'body_add_5', 'heading_add_6' ,  'snap_add_6' , 'body_add_6', 'heading_add_7' ,  'body_add_7'] #describe the field need to create 
	template_name = 'geeks/coursearticle_update.html'
	success_url = reverse_lazy('geeks-coursearticle')


class CoursearticleDeleteView(LoginRequiredMixin, DeleteView):
	model = CourseArticle
	success_url = reverse_lazy('geeks-coursearticle')

# geeks-question-list

class questionListView(ListView): # turns to announcment
    model = Quicklearn
    template_name = 'geeks/quicklearn_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'question'
    ordering = ['-published_on']
  

class questionCreateView(LoginRequiredMixin, CreateView):
	model = Quicklearn
	fields = ['topic' , 'meta', 'tags' , 'question' , 'keynote' , 'answer'] #describe the field need to create 
	success_url = reverse_lazy('geeks-question')


# geeks-question-detail

class questionDetailView(LoginRequiredMixin, DetailView):
	model = Quicklearn
	template_name = 'geeks/quicklearn_detail.html'


class questionUpdateView(LoginRequiredMixin, UpdateView):
	model = Quicklearn
	fields = ['topic' , 'meta' ,  'tags' , 'question' , 'keynote' , 'answer'] #describe the field need to create 
	template_name = 'geeks/quicklearn_update.html'
	success_url = reverse_lazy('geeks-question')


class questionDeleteView(LoginRequiredMixin, DeleteView):
	model = Quicklearn
	success_url = reverse_lazy('geeks-question')



#search question view  (coursse lesson)
class SearchQuestionResultsListView(ListView): # turns to announcment
    model = Quicklearn
    template_name = 'landing/search_question_results.html' #<app>/<model>_<viewtype>.html

    def get_queryset(self):
    	query = self.request.GET.get("q")
    	object_list = Quicklearn.objects.filter(
    		Q(topic__icontains=query) | Q(question__icontains=query) |  Q(tags__icontains=query)
    		)
    	return object_list 


# geeks-blog-article-list

class blogListView(ListView): # turns to announcment
    model = BlogArticle
    template_name = 'geeks/blogarticle_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'blogarticle'
    ordering = ['-published_on']
  

class blogCreateView(LoginRequiredMixin, CreateView):
	model = BlogArticle
	fields = ['course', 'standard' , 'meta' , 'title' , 'keynote' ,'snap', 'body', 'tags', 'heading_add_1' ,  'snap_add_1' , 'body_add_1'
	,'heading_add_2' , 'snap_add_2' , 'body_add_2','heading_add_3' , 'snap_add_3' , 'body_add_3','heading_add_4' , 'snap_add_4' , 'body_add_4','heading_add_5' , 'snap_add_5' , 'body_add_5','heading_add_6'  , 'snap_add_6' , 'body_add_6', 'heading_add_7' , 'body_add_7' ,'videofile'] #describe the field need to create 
	success_url = reverse_lazy('geeks-blog')


# geeks-question-detail

class blogDetailView(LoginRequiredMixin, DetailView):
	model = BlogArticle
	template_name = 'geeks/blogarticle_detail.html'


class blogUpdateView(LoginRequiredMixin, UpdateView):
	model = BlogArticle
	fields = ['course', 'standard' , 'title' , 'meta' , 'keynote' ,'snap', 'body', 'tags', 'heading_add_1' ,  'snap_add_1' , 'body_add_1'
	, 'heading_add_2' ,  'snap_add_2' , 'body_add_2', 'heading_add_3' ,  'snap_add_3' , 'body_add_3',  'heading_add_4' , 'snap_add_4' , 'body_add_4', 'heading_add_5' ,  'snap_add_5' , 'body_add_5',  'heading_add_6' , 'snap_add_6' , 'body_add_6',  'heading_add_7' , 'body_add_7' ,'videofile' ] #describe the field need to create 
	template_name = 'geeks/blogarticle_update.html'
	success_url = reverse_lazy('geeks-blog')


class blogDeleteView(LoginRequiredMixin, DeleteView):
	model = BlogArticle
	success_url = reverse_lazy('geeks-blog')



# geeks-video-lesson-list

class videolessonListView(LoginRequiredMixin, ListView): # turns to announcment
    model = Geeksvideo
    template_name = 'geeks/geeksvideo_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'videolesson'
    ordering = ['-published_on']
  

class videolessonCreateView(LoginRequiredMixin, CreateView):
	model = Geeksvideo
	fields = ['topic', 'standard' , 'body' , 'tags' , 'videofile', 'thumbnail'] #describe the field need to create 
	success_url = reverse_lazy('geeks-video')


# geeks-videolesson-detail

class videolessonDetailView(LoginRequiredMixin, DetailView):
	model = Geeksvideo
	template_name = 'geeks/geeksvideo_detail.html'


class videolessonUpdateView(LoginRequiredMixin, UpdateView):
	model = Geeksvideo
	fields = ['topic', 'standard' , 'body' , 'tags' , 'videofile', 'thumbnail'] #describe the field need to create 
	template_name = 'geeks/geeksvideo_update.html'
	success_url = reverse_lazy('geeks-video')


class videolessonDeleteView(LoginRequiredMixin, DeleteView):
	model = Geeksvideo
	success_url = reverse_lazy('geeks-video')




# geeks-books-lesson-list

class booksListView(ListView): # turns to announcment
    model = ebook
    template_name = 'geeks/ebook_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'book'
    ordering = ['-published_on']
  

class booksCreateView(LoginRequiredMixin, CreateView):
	model = ebook
	fields = ['topic', 'standard' , 'body' , 'tags' , 'bookfile', 'snap'] #describe the field need to create 
	success_url = reverse_lazy('geeks-ebook')


# geeks-videolesson-detail

class booksDetailView(LoginRequiredMixin, DetailView):
	model = ebook
	template_name = 'geeks/ebook_detail.html'


class booksUpdateView(LoginRequiredMixin, UpdateView):
	model = ebook
	fields = ['topic', 'standard' , 'body' , 'tags' , 'bookfile', 'snap'] #describe the field need to create 
	template_name = 'geeks/ebook_update.html'
	success_url = reverse_lazy('geeks-ebook')


class booksDeleteView(LoginRequiredMixin, DeleteView):
	model = ebook
	success_url = reverse_lazy('geeks-blog')




@login_required
def course_bookmark_add(request , id):
	course = get_object_or_404(Course , id=id)
	if course.coursebookmark.filter(id=request.user.id).exists():
		course.coursebookmark.remove(request.user)
	else:
		course.coursebookmark.add(request.user)
	return redirect('course-bookmark-list')



@login_required
#@cache_page(60 * 15)
def course_bookmark_list(request):
	enrolled = Course.objects.filter(coursebookmark=request.user)
	return render(request, 'geeks/enrolled_list.html' , {'enrolled':enrolled})




@login_required
def lesson_bookmark_add(request , id):
	lesson = get_object_or_404(CourseArticle , id=id)
	if lesson.lessonbookmark.filter(id=request.user.id).exists():
		lesson.lessonbookmark.remove(request.user)
	else:
		lesson.lessonbookmark.add(request.user)
	return redirect('coursearticle-detail', lesson.pk)


@login_required
#@cache_page(60 * 15)
def lesson_bookmark_list(request):
	saved_lesson = CourseArticle.objects.filter(lessonbookmark=request.user)
	return render(request, 'geeks/savelesson_list.html' , {'saved_lesson':saved_lesson})



@login_required
def question_bookmark_add(request , id):
	save = get_object_or_404(Quicklearn , id=id)
	if save.quesbookmark.filter(id=request.user.id).exists():
		save.quesbookmark.remove(request.user)
	else:
		save.quesbookmark.add(request.user)
	return redirect('question-detail', save.pk)

@login_required
#@cache_page(60 * 15)
def question_bookmark_list(request):
	saved = Quicklearn.objects.filter(quesbookmark=request.user)
	return render(request, 'geeks/save_list.html' , {'saved':saved})


@login_required
def video_bookmark_add(request , id):
	save = get_object_or_404(Geeksvideo , id=id)
	if save.videobookmark.filter(id=request.user.id).exists():
		save.videobookmark.remove(request.user)
	else:
		save.videobookmark.add(request.user)
	return redirect('geeks-video')

@login_required
#@cache_page(60 * 15)
def video_bookmark_list(request):
	saved = Geeksvideo.objects.filter(videobookmark=request.user)
	return render(request, 'geeks/savevideo_list.html' , {'saved':saved})


'''
class AddBloglike(LoginRequiredMixin, View):
	def blogarticle (self, request,pk,*args, **kwargs):
		blog = BlogArticle.objects.get(pk=pk)
		is_blogdislikes = False

		for blogdislikes in blog.blogdislikes.all():
			if blogdislikes == request.user:
				is_blogdislikes = True
				break

			if is_blogdislikes:
				blog.blogdislikes.remove(request.user)

		is_bloglikes = False

		for bloglikes in blog.bloglikes.all() :
			if bloglikes == request.user :
				is_bloglikes = True
				break

			if not is_bloglike :
				blog.bloglikes.add(request.user)
			if is_bloglikes :
				blog.bloglikes.remove(request.user)

			


class AddBlogdislike(LoginRequiredMixin, View):
	def blogarticle (self, request,pk,*args, **kwargs):
		blog = BlogArticle.objects.get(pk=pk)
		is_bloglikes = False

		for bloglikes in blog.bloglikes.all():
			if like == request.user:
				is_bloglikes = True
				break

			if is_bloglikes:
				blog.bloglikes.remove(request.user)

		is_blogdislikes = False

		for blogdislikes in blog.blogdislikes.all() :
			if blogdislikes == request.user :
				is_blogdislikes = True
				break

			if not is_blogdislikes :
				blog.blogdislikes.add(request.user)
			if is_blogdislikes :
				blog.blogdislikes.remove(request.user)

'''

