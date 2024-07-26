from django import forms
from .models import *

class CourseUpdateForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Course
        fields = "__all__"


class CoursearticleUpdateForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = CourseArticle
        fields = "__all__"


class BlogarticleUpdateForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = BlogArticle
        fields = "__all__"

