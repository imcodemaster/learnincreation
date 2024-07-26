from django.shortcuts import render
from .models import * 
from django.shortcuts import get_object_or_404
from django.views.generic import View, ListView, DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin #importing loginrequiredMixin and UserPassesTestMixin from auth.mixin
from django.contrib.auth.models import User #import User from models
from django.urls import reverse_lazy , reverse
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .render import Render
from django.views import View




def NoteLikeView(request , pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    got_liked = False
    if post.notelikes.filter(id=request.user.id).exists():
        post.notelikes.remove(request.user)
        got_liked = False
    else:
        post.notelikes.add(request.user)
        got_liked = True
    return HttpResponseRedirect(reverse('post-detail' , args=[str(pk)]))


def FileLikeView(request , pk):
    file = get_object_or_404(fileshare, id=request.POST.get('fileshare_id'))
    got_liked = False
    if file.likes.filter(id=request.user.id).exists():
        file.likes.remove(request.user)
        got_liked = False
    else:
        file.likes.add(request.user)
        got_liked = True
    return HttpResponseRedirect(reverse('file-detail' , args=[str(pk)]))

'''
def VideoLikeView(request , pk):
    videos = get_object_or_404(video, id=request.POST.get('video_id'))
    got_liked = False
    if videos.likes.filter(id=request.user.id).exists():
        videos.likes.remove(request.user)
        got_liked = False
    else:
        videos.likes.add(request.user)
        got_liked = True
    return HttpResponseRedirect(reverse('video-detail' , args=[str(pk)]))

'''

class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'post' , 'user'
    ordering = ['-published']
    paginate_by = 10


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'post/post_detail.html' #<app>/<model>_<viewtype>.html
    
    def get_context_data(self , *args , **kwargs):
        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        got_liked = False
        if stuff.notelikes.filter(id = self.request.user.id).exists():
            got_liked = True

        context = super(PostDetailView , self).get_context_data( *args , **kwargs)
        context ['objects_name'] = 'post'
        context ['total_likes'] = total_likes
        context ['got_liked'] = got_liked
        return context
    

class FileDetailView(LoginRequiredMixin,DetailView):
    model = fileshare
    template_name = 'post/fileshare_detail.html' #<app>/<model>_<viewtype>.html
    
    def get_context_data(self , *args , **kwargs):
        stuff = get_object_or_404(fileshare, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        got_liked = False
        
        if stuff.likes.filter(id = self.request.user.id).exists():
            got_liked = True
        context = super(FileDetailView , self).get_context_data( *args , **kwargs)
        context ['objects_name'] = 'fileshare'
        context ['total_likes'] = total_likes
        context ['got_liked'] = got_liked
        return context

'''

class VideoDetailView(LoginRequiredMixin,DetailView):
    model = video
    template_name = 'post/video_detail.html' #<app>/<model>_<viewtype>.html
    
    def get_context_data(self , *args , **kwargs):
        stuff = get_object_or_404(video, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        got_liked = False
        
        if stuff.likes.filter(id = self.request.user.id).exists():
            got_liked = True
        context = super(VideoDetailView , self).get_context_data( *args , **kwargs)
        context ['objects_name'] = 'video'
        context ['total_likes'] = total_likes
        context ['got_liked'] = got_liked
        return context

'''


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post #describing models 
    fields = ['subject', 'about' ,  'course' , 'semester' , 'subjects' , 'content' , 'content_addition' , 'highlight' ,"image"  ] #describe the field need to create 
    success_url = reverse_lazy('post-list')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView,):
    model = Post
    fields = ['subject', 'about' ,  'course' , 'semester' , 'subjects' , 'content' ,'content_addition', 'highlight' ,"image"  ] #describe the field need to Update
    success_url = reverse_lazy('post-list')
    
    def form_valid(self,form):

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):

        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False 

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView,):
    model = Post
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 



def postsearch(request):

    try:
        query = request.GET.get('querypost')
    except:
        query = None

    if query :
        query = request.GET.get('querypost').lower()
        template = 'post/postresults.html'
        postresult = [item for item in Post.objects.filter(subject__icontains = query) if query in item.subject.lower()]



    else:
        template = 'post/post-list.html'
        postresult = {}

    return render(request, template, {"postresult": postresult })

'''

def videosearch(request):

    try:
        query = request.GET.get('queryvideo')
    except:
        query = None

    if query :
        query = request.GET.get('queryvideo').lower()
        template = 'post/videoresults.html'
        videoresult = [item for item in video.objects.filter(subject__icontains = query) if query in item.subject.lower()]



    else:
        template = 'post/video-list.html'
        videoresult = {}

    return render(request, template, {"videoresult": videoresult })
'''

def filesearch(request):

    try:
        query = request.GET.get('queryfile')
    except:
        query = None

    if query :
        query = request.GET.get('queryfile').lower()
        template = 'post/fileresults.html'
        fileresult = [item for item in fileshare.objects.filter(subject__icontains = query) if query in item.subject.lower()]



    else:
        template = 'post/fileshare_list.html'
        fileresult = {}

    return render(request, template, {"fileresult": fileresult })


class FileListView(ListView):
    model = fileshare
    template_name = 'post/fileshare_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'fileshare' , 'user'
    ordering = ['-published']
    paginate_by = 10



class FileCreateView(LoginRequiredMixin, CreateView):
    model = fileshare #describing models 
    fields = ['subject', 'about' , 'course' , 'semester' , 'subjects'  , 'content' ,  'choose_file' , 'highlight' ] #describe the field need to create 
    success_url = reverse_lazy('file-list')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class FileDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView,):
    model = fileshare
    success_url = reverse_lazy('file-list')

    def test_func(self):
        fileshare = self.get_object()
        if self.request.user == fileshare.author:
            return True
        return False 

'''
class VideoListView(ListView):
    model = video
    template_name = 'post/video_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'Video' , 'user'
    ordering = ['-published']
    paginate_by = 10



class VideoCreateView(LoginRequiredMixin, CreateView):
    model = video #describing models 
    fields = ['subject', 'about' , 'course' , 'semester' , 'subjects' , 'content', 'highlight' , 'video' ] #describe the field need to create 
    success_url = reverse_lazy('video-list')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class VideoDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView,):
    model = video
    success_url = reverse_lazy('video-list')

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.author:
            return True
        return False 


'''
# fees_manangement ====================
#===========================================

#=================================================
#=================================================
class PostCommentCreateView(LoginRequiredMixin, CreateView):
    model = PostComment #describing models 
    fields = ['comment_content'] #describe the field need to create 
    #ordering = ['published']
    template_name = 'post/postcomment_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)


class FileCommentCreateView(LoginRequiredMixin, CreateView):
    model = FileComment #describing models 
    fields = ['comment_content'] #describe the field need to create 
    #ordering = ['published']
    template_name = 'post/filecomment_form.html'
    success_url = reverse_lazy('file-list')

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)

'''
class VideoCommentCreateView(LoginRequiredMixin, CreateView):
    model = VideoComment #describing models 
    fields = ['comment_content'] #describe the field need to create 
    #ordering = ['published']
    template_name = 'post/videocomment_form.html'
    success_url = reverse_lazy('video-list')

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)
'''


class postpdfView(View):

    def get(self, request):
        pdfbook = Post.objects.filter(author = request.user)
        today = timezone.now()
    
        params = {
            'today': today,
            'pdfbook': pdfbook,
            'request': request
            }
        return Render.render( '../templates/post/pdfbook_pdf.html',  params)    

