from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 
from django.utils import timezone
from django.db.models import Avg, Count, Min, Sum
# Create your models here.


Course = [
				('Junior Class' , "Junior Class"),
				('10th Class' , "10th Class"),
				('11th Class' , "11th Class"),
				('12th Class' , "12th Class"),
				('B.Sc', "B.Sc"),
				('B.Com', "B.Com"),
				('B.A', "B.A"),
				('BBA', "BBA"),
				('MBA', "MBA"),
				('B.Ed', "B.Ed"),
				('M.Ed', "M.Ed"),
				('M.Sc' , "M.Sc"),
				('M.Com' , "M.Com"),
				('M.A' , "M.A"),
				('Additional Information' , "Additional Information")
				
		]

Subjects = [
				('Physics', "Physics"),
				('Chemistry', "Chemistry"),
				('Zoology', "Zoology"),
				('Statistics', "Statistics"),
				('Maths', "Maths"),
				('English', "English"),
				('Hindi', "Hindi"),
				('Sanskrit' , "Sanskrit"),
				('Sociology' , "Sociology"),
				('Computer Science' , "Computer Science"),
				('Sociology' , "Sociology"),
				
		]


Semester = [
				('Additional Information', "Additional Information"),
				('1 Semester', "1 Semester"),
				('2 Semester', "2 Semester"),
				('3 Semester', "3 Semester"),
				('4 Semester', "4 Semester"),
				('5 Semester', "5 Semester"),
				('6 Semester', "6 Semester")
		]




class Post(models.Model):
	subject = models.CharField(max_length = 100)
	about = models.CharField(max_length = 100, null= True , blank = True) #remove null when go to deploy

	course = models.CharField( max_length = 35 , choices=Course , null=True , blank=True)
	semester = models.CharField( max_length = 25 , choices=Semester , null=True , blank=True)
	subjects = models.CharField( max_length = 25 , choices=Subjects , null=True , blank=True)	
	published = models.DateTimeField(default = timezone.now)
	image = models.FileField(upload_to ='media' , null= True , blank = True)	
	content = models.TextField( null= True , blank = True)
	content_addition = models.TextField( null= True , blank = True)
	highlight = models.CharField( max_length = 500, null= True , blank = True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	#favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
	notelikes = models.ManyToManyField(User, related_name='notelike', default=None, blank=True)
	#like_count = models.BigIntegerField(default='0')		

	def total_likes(self):
		return self.notelikes.count()



	def __str__(self):
		return self.subject


	@property
	def mediaURL(self):
		try : 
			url = self.image.url
		except : 
			url = ''
		return url 



class fileshare(models.Model):
	subject = models.CharField(max_length = 100)
	about = models.CharField(max_length = 100, null= True , blank = True) #remove null when go to deploy
	course = models.CharField( max_length = 25 , choices=Course , null=True , blank=True)
	semester = models.CharField( max_length = 23 , choices=Semester , null=True , blank=True)
	subjects = models.CharField( max_length = 25 , choices=Subjects , null=True , blank=True)	
	published = models.DateTimeField(default = timezone.now)
	highlight = models.CharField( max_length = 500, null= True , blank = True)
	choose_file = models.FileField( null= True , blank = True)
	content = models.TextField( null= True , blank = True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	likes = models.ManyToManyField(User, related_name='filelike', default=None, blank=True)
	
	def total_likes(self):
		return self.likes.count()


	def __str__(self):
		return self.subject


	@property
	def mediaURL(self):
		try : 
			url = self.file.url
		except : 
			url = ''
		return url 
'''
class video(models.Model):
	subject = models.CharField(max_length = 100)
	about = models.CharField(max_length = 100, null= True , blank = True) #remove null when go to deploy
	highlight = models.CharField( max_length = 500, null= True , blank = True)
	
	course = models.CharField( max_length = 15 , choices=Course , null=True , blank=True)
	semester = models.CharField( max_length = 3 , choices=Semester , null=True , blank=True)
	subjects = models.CharField( max_length = 15 , choices=Subjects , null=True , blank=True)
	published = models.DateTimeField(default = timezone.now)
	content = models.TextField( null= True , blank = True)
	video = models.FileField( max_length = 500, null= True , blank = True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	likes = models.ManyToManyField(User, related_name='videolike', default=None, blank=True)

	def total_likes(self):
		return self.likes.count()



	def __str__(self):
		return self.subject


	@property
	def mediaURL(self):
		try : 
			url = self.video.url
		except : 
			url = ''
		return url 
'''


class PostComment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='postcomment' ,  on_delete=models.CASCADE)
	comment_content = models.TextField( null= True , blank = True)
	published = models.DateTimeField(default = timezone.now)




	def __str__(self):
		return self.user.username 


class FileComment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(fileshare, related_name='filecomment' ,  on_delete=models.CASCADE)
	comment_content = models.TextField( null= True , blank = True)
	published = models.DateTimeField(default = timezone.now)


	def __str__(self):
		return self.user.username 

'''

class VideoComment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(video, related_name='videocomment' ,  on_delete=models.CASCADE)
	comment_content = models.TextField(null= True , blank = True)
	published = models.DateTimeField(default = timezone.now)


	def __str__(self):
		return self.user.username 

'''
