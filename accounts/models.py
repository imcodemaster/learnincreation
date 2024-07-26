from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

standard = [
                ('Class 6th', "Class 6th"),
                ('Class 7th', "Class 7th"),
                ('Class 8th', "Class 8th"),
                ('Class 9th', "Class 9th"),
                ('Class 10th', "Class 10th"),
                ('Class 11th', "Class 11th"),
                ('Class 12th', "Class 12th"),
                ('Undergraduate', "Undergraduate"),
                ('Post-Undergraduate', "Post-Undergraduate"),
                ('Self Learner', "Self Learner"),
                
            
        ]

state = [
                ('Out side of India', "Out side of India"),
                ('Andaman and Nicobar Islands', "Andaman and Nicobar Islands"),
                ('Andhra Pradesh', "Andhra Pradesh"),
                ('Arunachal Pradesh', "Arunanchal Pradesh"),
                ('Assam', "Assam "),
                ('Bihar', "Bihar"),
                ('Chhattisgarh', "Chhattisgarh"),
                ('Chandigarh', "Chandigarh"),
                ('Dadra and Nagar Haveli', "Dadra and Nagar Haveli"),
                ('Daman and Diu', "Daman and Diu"),
                ('Delhi', "Delhi"),
                ('Goa', "Goa"),
                ('Gujrat', "Gujrat"),
                ('Haryana', "Haryana"),
                ('Himanchal Pradesh', "Himanchal Pradesh"),
                ('Jammu & Kashmir', "Jammu & Kashmir"),
                ('Jharkhand', "Jharkhand"),
                ('Karnataka', "Karnataka"),
                ('Kerela', "Kerela"),
                ('Ladakh', "Ladakh"),
                ('Lakshadweep', "Lakshadweep"),
                ('Madhya Pradesh', "Madhya Pradesh "),
                ('Maharastra', "Maharastra "),
                ('Manipur', "Manipur"),
                ('Meghalaya', "Meghalaya"),
                ('Mizoram', "Mizoram"),
                ('Nagaland', "Nagaland"),
                ('Odisha', " Odisha"),
                ('Punjab', " Punjab"),
                ('Puducherry', "Puducherry"),
                ('Rajasthan', "Rajasthan"),
                ('Sikkim', "Sikkim"),
                ('Tamil Naidu', "Tamil Naidu"),
                ('Telangana', "Telangana"),
                ('Tripura', "Tripura"),
                ('Uttar Pradesh', "Uttar Pradesh"),
                ('Uttarakhand', "Uttarakhand"),
                ('West Bengal', "West Bengal"),

        ]


countries = [
                
                ('India', "India"),
                ('Europe Continent', "Europe Continent"),
                ('Africa Continent', "Africa Continent"),
                ('Australia Continent', "Australia Continent"),
                ('Asia Continent', "Asia Continent"),
                ('North America Continent', "North America Continent"),
                ('South America Continent', "South America Continent"),
        ]


board = [
                
                ('Central Board of Secondary Education', "Central Board of Secondary Education"),
                ('ICSE Board', "ICSE Board"),
                ('State Board', "State Board"),
                ('Outside of India', "Outside of India"),
                ('Learning by Myself', "Learning by Myself"),
            
        ]


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, blank=True, null= True)
    mobile = models.CharField(max_length=10, blank=True, null= True)
    birth_date = models.DateField(null=True, blank=True)
    standard = models.CharField( max_length=30 , choices=standard , null=True , blank=True)
    academicbackground = models.CharField( max_length=40, choices=board , null=True , blank=True)    
    school_name = models.CharField(max_length=250, blank=True, null= True)
    address = models.CharField(max_length=250, blank=True, null= True)
    location = models.CharField(max_length=100 , choices=state, blank=True, null=True)
    country = models.CharField(max_length=100 , choices=countries, blank=True, null=True)
    picture = models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.png', null=True, blank=True)
    follower = models.ManyToManyField(User, blank=True, related_name='follower')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save() 
