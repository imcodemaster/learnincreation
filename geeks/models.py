from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from autoslug import AutoSlugField


# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=500, blank=True)
	standard = models.CharField(max_length=50, blank=True)
	slug = AutoSlugField(populate_from='name')
	meta = models.TextField(null=True,blank=True)
	description = models.CharField(max_length=500, blank=True)
	detail = models.TextField(null=True,blank=True)
	tags = models.CharField(max_length= 100, blank=True, null=True)
	snap = models.ImageField(upload_to='course/images_uploaded',null=True, blank=True)
	videofile = models.FileField(upload_to='uploads/videos_uploaded',null=True, blank=True)
	published_on = models.DateTimeField(default=timezone.now)
	courselikes = models.ManyToManyField(User, blank=True, related_name="courselikes")
	coursedislikes = models.ManyToManyField(User, blank=True, related_name="coursedislikes")
	courseenroll = models.ManyToManyField(User, blank=True, related_name="courseenroll")
	coursebookmark = models.ManyToManyField(User, blank=True, related_name="coursebookmark")

	def __str__(self):
		return self.name

class ebook(models.Model):
	topic = models.CharField(max_length=150, blank=True, null=True)
	slug = AutoSlugField(populate_from='topic')
	standard = models.CharField(max_length=50, blank=True)
	body = models.CharField(max_length=500, blank=True, null=True)
	tags = models.CharField(max_length= 100, blank=True, null=True)
	snap = models.ImageField(upload_to='ebook/images_uploaded',null=True, blank=True)
	ebookmark = models.ManyToManyField(User, blank=True, related_name="ebookmark")
	published_on = models.DateTimeField(default=timezone.now)
	

	def __str__(self):
		return self.topic

class Geeksvideo(models.Model):
	topic = models.CharField(max_length=150, blank=True, null=True)
	slug = AutoSlugField(populate_from='topic')
	standard = models.CharField(max_length=50, blank=True)
	body = models.TextField( blank=True, null=True)
	tags = models.CharField(max_length= 100, blank=True, null=True)
	videofile = models.CharField(max_length=500, blank=True, null=True)
	thumbnail = models.ImageField(upload_to='uploads/video_thumbnail',null=True, blank=True)
	videobookmark = models.ManyToManyField(User, blank=True, related_name="videobookmark")	
	published_on = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.topic


class CourseArticle(models.Model):
	course = models.ForeignKey(Course, on_delete = models.CASCADE)
	standard = models.CharField(max_length=50, blank=True)
	meta = models.TextField(blank=True, null=True)
	title = models.CharField(max_length=150, blank=True, null=True)
	slug = AutoSlugField(populate_from='title')
	keynote = models.CharField(max_length=500, blank=True, null=True)
	body = models.TextField(blank=True, null=True)

	heading_add_1 = models.CharField(max_length=250, blank=True, null=True)
	heading_add_2 = models.CharField(max_length=250, blank=True, null=True)
	heading_add_3 = models.CharField(max_length=250, blank=True, null=True)
	heading_add_4 = models.CharField(max_length=250, blank=True, null=True)
	heading_add_5 = models.CharField(max_length=250, blank=True, null=True)
	heading_add_6 = models.CharField(max_length=250, blank=True, null=True)
	heading_add_7 = models.CharField(max_length=250, blank=True, null=True)
	body_add_1 = models.TextField(blank=True, null=True)
	body_add_2 = models.TextField(blank=True, null=True)
	body_add_3 = models.TextField(blank=True, null=True)
	body_add_4 = models.TextField(blank=True, null=True)
	body_add_5 = models.TextField(blank=True, null=True)
	body_add_6 = models.TextField(blank=True, null=True)
	body_add_7 = models.TextField(blank=True, null=True)
	tags = models.CharField(max_length= 100, blank=True, null=True)
	snap = models.ImageField(upload_to='uploads/article/images_uploaded',null=True, blank=True)
	snap_add_1 = models.ImageField(upload_to='uploads/article/images_uploaded',null=True, blank=True)
	snap_add_2 = models.ImageField(upload_to='uploads/article/images_uploaded',null=True, blank=True)
	snap_add_3 = models.ImageField(upload_to='uploads/article/images_uploaded',null=True, blank=True)
	snap_add_4 = models.ImageField(upload_to='uploads/article/images_uploaded',null=True, blank=True)
	snap_add_5 = models.ImageField(upload_to='uploads/article/images_uploaded',null=True, blank=True)
	snap_add_6 = models.ImageField(upload_to='uploads/article/images_uploaded',null=True, blank=True)
	lessonbookmark = models.ManyToManyField(User, blank=True, related_name="lessonbookmark")
	published_on = models.DateTimeField(default=timezone.now)
	

	def __str__(self):
		return self.title or ''
	
	

class BlogArticle(models.Model):
	course = models.CharField(max_length=500, blank=True, null=True)
	standard = models.CharField(max_length=50, blank=True)
	title = models.CharField(max_length=150, blank=True, null=True)
	slug = AutoSlugField(populate_from='title')
	keynote = models.CharField(max_length=500, blank=True, null=True)
	body = models.TextField(blank=True, null=True)
	meta = models.TextField(blank=True, null=True)
	heading_add_1 = models.CharField(max_length=250, blank=True, null=True)
	heading_add_2 = models.CharField(max_length=250, blank=True, null=True)
	heading_add_3 = models.CharField(max_length=250, blank=True, null=True)
	heading_add_4 = models.CharField(max_length=250, blank=True, null=True)
	heading_add_5 = models.CharField(max_length=250, blank=True, null=True)
	heading_add_6 = models.CharField(max_length=250, blank=True, null=True)
	heading_add_7 = models.CharField(max_length=250, blank=True, null=True)
	body_add_1 = models.TextField(blank=True, null=True)
	body_add_2 = models.TextField(blank=True, null=True)
	body_add_3 = models.TextField(blank=True, null=True)
	body_add_4 = models.TextField(blank=True, null=True)
	body_add_5 = models.TextField(blank=True, null=True)
	body_add_6 = models.TextField(blank=True, null=True)
	body_add_7 = models.TextField(blank=True, null=True)
	tags = models.CharField(max_length= 100, blank=True, null=True)
	snap = models.ImageField(upload_to='uploads/article/images_uploaded',null=True, blank=True)
	videofile = models.FileField(upload_to='uploads/article/videos_uploaded',null=True, blank=True)
	blogbookmark = models.ManyToManyField(User, blank=True, related_name="blogbookmark")
	published_on = models.DateTimeField(default=timezone.now)
	

	def __str__(self):
		return self.title

class Quicklearn(models.Model):
	topic = models.CharField(max_length=50, blank=True, null=True)
	slug = AutoSlugField(populate_from='topic')
	meta = models.TextField(null=True,blank=True)
	tags = models.CharField(max_length= 100, blank=True, null=True)
	question = models.CharField(max_length=500, blank=True, null=True)
	keynote = models.CharField(max_length=200, blank=True, null=True)
	answer = models.TextField(blank=True, null=True)
	quesbookmark = models.ManyToManyField(User, blank=True, related_name="quesbookmark")	
	published_on = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.topic

class CoursePlaylist(models.Model):
	course = models.ForeignKey(Course, on_delete = models.CASCADE)
	standard = models.CharField(max_length=50, blank=True)
	title = models.CharField(max_length=150, blank=True, null=True)
	slug = AutoSlugField(populate_from='title')
	keynote = models.CharField(max_length=500, blank=True, null=True)
	videofile = models.CharField(max_length=500, blank=True, null=True)
	thumbnail = models.ImageField(upload_to='uploads/video_thumbnail',null=True, blank=True)
	body = models.TextField(blank=True, null=True)
	tags = models.CharField(max_length= 100, blank=True, null=True)
	published_on = models.DateTimeField(default=timezone.now)
	

	def __str__(self):
		return self.title

