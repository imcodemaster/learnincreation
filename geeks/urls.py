# -*- coding: utf-8 -*-

from django.urls import path
from . import views

from geeks.views import *


urlpatterns = [
    path('home/', views.geeks_home , name='geeks-home' ),
    path('pathway/', views.pathway, name='pathway'),
    path('geeks-courses/', CourseListView.as_view(), name='geeks-courses'),
    path('category/<int:cat_id>/', views.category, name='category'),
    #path('geeks-course-lesson/', views.lessonlist, name='geeks-courses-enrolled'),
    path('geeks-courses/new', CourseCreateView.as_view(), name='course-create'),
    path('geeks-courses/<slug>', CourseDetailView.as_view(), name='course-detail'),
    path('geeks-courses/<slug>/update', CourseUpdateView.as_view(), name='course-update'),
    path('geeks-courses/<slug>/delete', CourseDeleteView.as_view(), name='course-delete'),
    path('course-enrolled/<int:id>/', views.course_bookmark_add, name='course-bookmark'),
    path('geeks-courses/my-courses/', views.course_bookmark_list, name='course-bookmark-list'),
    path('geeks-courses-lesson/', CoursearticleListView.as_view(), name='geeks-coursearticle'),
    path('geeks-courses-lesson/new', CoursearticleCreateView.as_view(), name='coursearticle-create'),
    path('geeks-courses-lesson/<int:pk>', CoursearticleDetailView.as_view(), name='coursearticle-detail'),
    path('geeks-courses-lesson/<int:pk>/update', CoursearticleUpdateView.as_view(), name='coursearticle-update'),
    path('geeks-courses-lesson/<int:pk>/delete', CoursearticleDeleteView.as_view(), name='coursearticle-delete'),
    path('lesson-saved/<int:id>/', views.lesson_bookmark_add, name='lesson-bookmark'),
    path('geeks-courses/my-courses-lesson/', views.lesson_bookmark_list, name='lesson-bookmark-list'),
    path('video-saved/<int:id>/', views.video_bookmark_add, name='video-bookmark'),
    path('geeks-courses/my-video-lesson/', views.video_bookmark_list, name='video-bookmark-list'),
    path('geeks-video-lesson/', videolessonListView.as_view(), name='geeks-video'),
    path('geeks-video-lesson/new', videolessonCreateView.as_view(), name='geeksvideo-create'),
    path('geeks-video-lesson/<int:pk>', videolessonDetailView.as_view(), name='geeksvideo-detail'),
    path('geeks-video-lesson/<int:pk>/update', videolessonUpdateView.as_view(), name='geeksvideo-update'),
    path('geeks-video-lesson/<int:pk>/delete', videolessonDeleteView.as_view(), name='geeksvideo-delete'),
    path('geeks-question/', questionListView.as_view(), name='geeks-question'),
    path('geeks-question/new', questionCreateView.as_view(), name='question-create'),
    path('geeks-question/<int:pk>', questionDetailView.as_view(), name='question-detail'),
    path('geeks-question/<int:pk>/update', questionUpdateView.as_view(), name='question-update'),
    path('geeks-question/<int:pk>/delete', questionDeleteView.as_view(), name='question-delete'),
    path('saved/<int:id>/', views.question_bookmark_add, name='quick-save'),
    path('geeks-courses/quick-revision/', views.question_bookmark_list, name='save-list'),
    path('geeks-blog/', blogListView.as_view(), name='geeks-blog'),
    path('geeks-blog/new', blogCreateView.as_view(), name='blog-create'),
    path('geeks-blog/<slug>', blogDetailView.as_view(), name='blog-detail'),
    path('geeks-blog/<slug>/update', blogUpdateView.as_view(), name='blog-update'),
    path('geeks-blog/<slug>/delete', blogDeleteView.as_view(), name='blog-delete'),
    #path('geeks-blog/<int:pk>/like', AddBloglike.as_view(), name = 'blog-like'),
    #path('geeks-blog/<int:pk>/dislike', AddBlogdislike.as_view(), name = 'blog-dislike'),
    path('geeks-course-ebook/', booksListView.as_view(), name='geeks-ebook'),
    path('geeks-course-ebook/new', booksCreateView.as_view(), name='ebook-create'),
    path('geeks-course-ebook/<int:pk>', booksDetailView.as_view(), name='ebook-detail'),
    path('geeks-course-ebook/<int:pk>/update', booksUpdateView.as_view(), name='ebook-update'),
    path('geeks-course-ebook/<int:pk>/delete', booksDeleteView.as_view(), name='ebook-delete'),
    path('download-question-answer-pdf/', lessonpdfView.as_view(), name = 'lessonpdf'),
	path('download-lesson-pdf/',courselessonpdfView.as_view(), name = 'courselessonpdf'),
	path('q/', SearchQuestionResultsListView.as_view(), name='search-question-results'),
]

