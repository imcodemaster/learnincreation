from django.contrib import admin
from .models import Post , fileshare  , PostComment , FileComment 
from django.contrib.admin.options import ModelAdmin


# Register your models here.
class PostAdmin(ModelAdmin):
	list_display = ['subject','published', 'author']
	search_field = ['author']
	list_filter = [ 'author', 'published']


admin.site.register(Post, PostAdmin)

class PostCommentAdmin(ModelAdmin):
	list_display = ['user','post','published', 'comment_content']
	search_field = ['user','post',]
	list_filter = [ 'user', 'published' ,'post',]


admin.site.register(PostComment, PostCommentAdmin)


class FileCommentAdmin(ModelAdmin):
	list_display = ['user','post','published', 'comment_content']
	search_field = ['user','post',]
	list_filter = [ 'user', 'published' ,'post',]


admin.site.register(FileComment, FileCommentAdmin)

'''
class VideoCommentAdmin(ModelAdmin):
	list_display = ['user','post','published', 'comment_content']
	search_field = ['user','post',]
	list_filter = [ 'user', 'published' ,'post',]


admin.site.register(VideoComment, VideoCommentAdmin)


'''


# Register your models here.
class fileshareAdmin(ModelAdmin):
	list_display = ['subject','published', 'author']
	search_field = ['author']
	list_filter = [ 'author', 'published']


admin.site.register(fileshare, fileshareAdmin)

'''

# Register your models here.
class videoAdmin(ModelAdmin):
	list_display = ['subject','published', 'author']
	search_field = ['author']
	list_filter = [ 'author', 'published']


admin.site.register(video, videoAdmin)


'''