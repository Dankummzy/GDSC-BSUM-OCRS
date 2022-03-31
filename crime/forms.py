from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Post, Report


class RegisterCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_image', 'post_body']


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['report_title', 'report_image', 'report_body', 'report_location']






