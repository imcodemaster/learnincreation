'''
Learnincreation model - main website


'''
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField

# Create your models here.



# Create your models here.

Department = [
                ('Support & Helpdesk Department', "Support & Helpdesk Department"),
                ('Report & Feedback Department', "Report & Feedback Department"),
                ('Customer Support Department', "Customer Support Department"),
                ('Accounts Department', "Accounts Department"),
                ('Share your Knowledge', "Share your Knowledge"),
                
        ]

subscribefor = [
                ('Build Business Profile', "Build Business Profile"),
                ('Free E-books & Updates', "Free E-books & Updates"),
                ('Free Sessions & Newsletter', "Free Sessions & Newsletter"),
				('Seminar and WorkShop', "Seminar and WorkShop"),
				('1 Month Workshop on Computer Proficiency For Office', "1 Month Workshop on Computer Proficiency For Office"),
                ('3 Month Proffessional Computer Certification Course', "3 Month Proffessional Computer Certification Course"),
                ('Send me all Updates', "Send me all Updates"),
            
        ]

center = [
                ('S.B.S. Govt. P.G. College, U.S.Nagar', "S.B.S. Govt. P.G. College, U.S.Nagar"),
                ('Institute of Management and Technology, Bindhukhera', "Institute of Management and Technology, Bindhukhera"),
                
        ]

course = [
                ('B.Sc 1 sem', "B.Sc 1 sem"),
				('B.Sc 2 year', "B.Sc 2 year"),
				('B.Sc 3 year', "B.Sc 3 year"),
                ('B.Com 1 sem', "B.Com 1 sem"),
				('B.Com 2 year', "B.Com 2 year"),
				('B.Com 3 year', "B.Com 3 year"),
				('B.A 1 sem', "B.A 1 sem"),
				('B.A 2 year', "B.A 2 year"),
				('B.A 3 year', "B.A 3 year"),
				('B.B.A 1 sem', "B.B.A 1 sem"),
				('B.B.A 3 sem', "B.B.A 3 sem"),
				('B.B.A 5 sem', "B.B.A 5 sem"),
				('M.Sc 1 year', "M.Sc 1 year"),
				('M.Sc 2 year', "M.Sc 2 year"),
				('M.Com 1 year', "M.Com 1 year"),
				('M.Com 2 year', "M.Com 2 year"),
				('M.A 1 year', "M.A 1 year"),
				('M.A 2 year', "M.A 2 year"),
				
        ]



#contact model for front end 

class Contact(models.Model):
    first_name = models.CharField(max_length = 100)
    second_name = models.CharField(max_length = 100)
    to_the_department = models.CharField( max_length = 30 , choices=Department , null=True , blank=True)
    email = models.EmailField() 
    mobile = models.CharField(max_length = 10)
    message = models.TextField()
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.first_name 



'''

# teacher model - faculty view

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField(null = True , blank = True)
    img = models.ImageField(null = True, blank = True)
    qualification = models.CharField(max_length=200)
    salary = models.FloatField()
    age = models.IntegerField()
    phonenumber = models.IntegerField() #without country code
    aadaharid = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)
	#slug = models.SlugField()

    def __str__(self):
        return self.name

    @property
    def imageURL(self): #imgUrl ke media se lelega .. /media/ wala
        try :
            url = self.img.url
        except:
        	url = ''
        return url

# department model - (dynamic department updation)

class Department(models.Model):
    name = models.CharField(max_length = 100)
    Subject_name1 = models.CharField(max_length = 100 , null = True , blank = True)
    Subject_name2 = models.CharField(max_length = 100 ,null = True , blank = True)
    Subject_name3 = models.CharField(max_length = 100 , null = True , blank = True)
    Subject_name4 = models.CharField(max_length = 100 ,null = True , blank = True)
    Subject_name5 = models.CharField(max_length = 100 , null = True , blank = True)
   
    hod_msg = models.TextField(null = True , blank = True)
    
    about = models.TextField(null = True , blank = True)
    hod_name =models.CharField(max_length= 50 , null = True , blank = True)
    hod_email = models.CharField(max_length = 50, null = True , blank = True)
    branch = models.CharField(max_length = 30 , null = True , blank = True )
 

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def mediaURL(self):
        try : 
            url = self.img.url
        except : 
            url = ''
        return url 

#our pride model  - encouragement view - 

class Pride(models.Model):
    student = models.CharField(max_length=100)
    detail = models.TextField(null = True , blank = True)
    img = models.ImageField(null = True, blank = True)
    qualification = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add = True)
    #slug = models.SlugField()

    def __str__(self):
        return self.student

    @property
    def imageURL(self):
        try :
            url = self.img.url
        except:
            url = ''
        return url


'''
class doodle(models.Model):
    tooltip = models.CharField(max_length=100)
    detail = models.TextField(null = True , blank = True)
    img = models.ImageField(null = True, blank = True , upload_to='uploads/doodle')
    event = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='event')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    likes = models.ManyToManyField(User, related_name='like', default=None, blank=True)
    like_count = models.BigIntegerField(default='0')
    moredetail = models.TextField(null = True , blank = True)

    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.event

    @property
    def imageURL(self):
        try :
            url = self.img.url
        except:
            url = ''
        return url


class Subscribe(models.Model):
    
    first_name = models.CharField(max_length = 100)
    second_name = models.CharField(max_length = 100)
    Subscription = models.CharField( max_length = 100 , choices=subscribefor , null=True , blank=True)
    email = models.EmailField()
    institute = models.CharField( max_length = 100 , choices=center , null=True , blank=True)
    course = models.CharField( max_length = 100 , choices=course , null=True , blank=True)
    registration_number = models.CharField(max_length = 30 , null=True , blank=True)
    mobile = models.CharField(max_length = 10)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
    	return self.first_name 


#notice model  - ntioce view  - news front end 
        

class Think(models.Model):
   
    title = models.CharField(max_length = 1000)
    published = models.DateTimeField(auto_now_add = True)
    author = models.CharField(max_length = 100)
   


    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title
