from django.urls import path
from . import views

from accounts.views import *
from django.contrib.auth import views as auth_views #import this

urlpatterns = [
 
    path('register/', views.register_request, name='registerpage'),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name= "logout"),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('setting/', views.setting, name='setting'),
    path('account-setting/', views.accountsetting, name='account-setting'),
    path('secure-your-account/', views.secure, name='secure'),
    path('profile/<int:pk>/follow/add-follower', Addfollower.as_view() , name = 'add-follower'),
    path('profile/<int:pk>/follow/unfollow', Removefollower.as_view() , name = 'remove-follower'),
    path('password_reset', views.password_reset_request, name="password_reset"),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password/password_reset_done.html') , name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name= 'accounts/password/password_reset_confirm.html') ,  name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(template_name= 'accounts/password/password_reset_complete.html')  , name='password_reset_complete'),
    
]

'''
    path('password_change/'   name='password_change'),
    path('password_change/done'  name='password_change_done'),
    path('password_reset/', ,name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password/password_reset_done.html') , name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name= 'accounts/password/password_reset_confirm.html') ,  name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(template_name= 'accounts/password/password_reset_complete.html')  , name='password_reset_complete'),    
    '''