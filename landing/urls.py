# -*- coding: utf-8 -*-

from django.urls import path
from . import views
from landing.views import *


urlpatterns = [
    path('', views.index, name='indexpage'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
	path('cyber-awareness-program/', views.cybersmart, name='becybersmart'),
    path('product/', views.product, name='product'),
    path('gallary/', views.gallary, name='gallary'),
    path('contact/', ContactView.as_view(), name = 'contact'),
    path('subscription/', SubscribeView.as_view(), name = 'subscribe'),
    path('thinkaboutit/' , ThinkListView.as_view() , name = "think-list"),
    path('pricing/', views.paymentpage, name='pricing'),
    path('shareyourknowledge/', views.shareyourknowledge, name='shareyourknowledge'),
    path('build-business-profile/', views.business, name='business'),
    path('privacy-policies/', views.policies, name='policy'),
    path('terms/', views.terms, name='terms'),
    path('explore/new/', doodleCreateView.as_view() , name = 'doodle-create' ),
    path('explore/' , doodlelistView.as_view() , name = "doodle-list"),
    path('explore/<int:pk>/', doodlelistDetailView.as_view() , name = 'doodle-detail' ),
    path('explore/<int:pk>/update/', doodleUpdateView.as_view() , name = 'doodle-update' ),
    path('explore/<int:pk>/delete/', doodleDeleteView.as_view() , name = 'doodle-delete' ),
    path('like/<int:pk>/', doodleLikeView , name = 'doodle-like' ),
    path('community-guidelines/', views.community, name='community'),
    path('pictures/', views.picture, name='pictures'),
    path('helpdesk/', views.helpdesk, name='helpdesk'),
    path('faq/', views.faq, name='faq'),
    path('q/', SearchResultsListView.as_view(), name='search-results'),
     #path('lesson/', views.postsearch, name="postsearch"),
    
    
]

'''
business profile url -- 

 path('business-around-me/', businessprofileView.as_view(), name='business-list'),
    path('business-profile/new', businessprofileCreateView.as_view(), name='business-profile-create'),
    path('business-profile/<int:pk>', businessprofileDetailView.as_view(), name='business-detail'),
    path('business-profile/<int:pk>/update', businessprofileUpdateView.as_view(), name='business-profile-update'),
    path('business-profile/<int:pk>/delete', businessprofileDeleteView.as_view(), name='business-profile-delete'),

'''