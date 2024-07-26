from django.contrib import admin
from .models import  Course, ebook, Geeksvideo, CourseArticle, BlogArticle, Quicklearn , CoursePlaylist
# Register your models here.


admin.site.register(Course)
admin.site.register(ebook)
admin.site.register(Geeksvideo)
admin.site.register(CourseArticle)
admin.site.register(CoursePlaylist)
admin.site.register(BlogArticle)
admin.site.register(Quicklearn)