from django.urls import path
from post import views 
from .views import *

urlpatterns = [


    path('post/' , PostListView.as_view() , name = "post-list"),
    path('file/' , FileListView.as_view() , name = "file-list"),
    #path('video/' , VideoListView.as_view() , name = "video-list"),
    path('post/<int:pk>/', PostDetailView.as_view() , name = 'post-detail' ),
    #path('video/<int:pk>/', VideoDetailView.as_view() , name = 'video-detail' ),
    path('file/<int:pk>/', FileDetailView.as_view() , name = 'file-detail' ),
   	path('like/<int:pk>/', NoteLikeView , name = 'post-like' ),
   	#path('videolike/<int:pk>/', VideoLikeView , name = 'video-like' ),
   	path('filelike/<int:pk>/', FileLikeView , name = 'file-like' ),
 	path('post/new/', PostCreateView.as_view() , name = 'post-create' ),
 	#path('video/new/', VideoCreateView.as_view() , name = 'video-create' ),
 	path('file/new/', FileCreateView.as_view() , name = 'file-create' ),
    path('post/<int:pk>/update/', PostUpdateView.as_view() , name = 'post-update' ),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() , name = 'post-delete' ),
    path('file/<int:pk>/delete/', FileDeleteView.as_view() , name = 'file-delete' ),
    #path('video/<int:pk>/delete/', VideoDeleteView.as_view() , name = 'video-delete' ),
    path('post/<int:pk>/comment', PostCommentCreateView.as_view() , name = 'post-comment' ),
    path('file/<int:pk>/comment', FileCommentCreateView.as_view() , name = 'file-comment' ),
    #path('video/<int:pk>/comment', VideoCommentCreateView.as_view() , name = 'video-comment' ),
    path('postpdf/', postpdfView.as_view(), name = 'postpdf'),
  
    path('file/', filesearch, name="filesearch"),
    path('post/', postsearch, name="postsearch"),
  

]





