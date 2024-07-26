from django.contrib import admin
from .models import Contact , Think, Subscribe , doodle
from django.contrib.admin.options import ModelAdmin


# Register your models here.
'''
class TeacherAdmin(ModelAdmin):
	list_display = ['name', 'qualification', 'phonenumber']
	search_field = ['name']
	list_filter = ['salary', 'qualification']

admin.site.register(Teacher, TeacherAdmin)

admin.site.register(Department)

class PrideAdmin(ModelAdmin):
	list_display = ['student', 'qualification']
	search_field = ['student']
	list_filter = ['qualification' , 'date']

admin.site.register(Pride, PrideAdmin)

'''


class ContactAdmin(ModelAdmin):
	list_display = ['to_the_department', 'first_name', 'second_name' , 'mobile' , 'email', 'message' , 'date']
	search_field = ['first_name' ,  'mobile' , 'email',]
	list_filter = [ 'mobile' , 'email',]

admin.site.register(Contact, ContactAdmin)

class ThinkAdmin(ModelAdmin):
	list_display = ['title', 'published']
	search_field = ['title', 'published']
	list_filter = ['title', 'published']

admin.site.register(Think, ThinkAdmin)


class SubscribeAdmin(ModelAdmin):
	list_display = ['first_name', 'second_name' , 'mobile', 'email', 'date']
	search_field = ['first_name' , 'second_name' , 'mobile', 'email',]
	list_filter = [ 'first_name' , 'second_name' , 'mobile', 'email',]

admin.site.register(Subscribe, SubscribeAdmin)

admin.site.register(doodle)

'''

class businessProfileAdmin(ModelAdmin):
	list_display = ['business_name', 'email' , 'mobile', 'location', 'description' ,  'date']
	search_field = ['business_name' , 'email' , 'mobile', 'location',]
	list_filter = [ 'business_name' , 'email' , 'mobile', 'location',]

admin.site.register(businessProfile, businessProfileAdmin)



'''