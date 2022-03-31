import requests
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import Post, Report
from .forms import RegisterCreationForm, PostForm, ReportForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import pyrebase
from django.core.paginator import Paginator
from django.contrib import auth


firebaseConfig = {
  'apiKey': "AIzaSyDnWyj2VeJ8vJEk6FbFIbFH9s6wj1gV_Fk",
  'authDomain': "my-ocrs-project.firebaseapp.com",
  'databaseURL': "https://my-ocrs-project-default-rtdb.firebaseio.com",
  'projectId': "my-ocrs-project",
  'storageBucket': "my-ocrs-project.appspot.com",
  'messagingSenderId': "488321946342",
  'appId': "1:488321946342:web:715a67cddeddef6009e127",
}


firebase = pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()
# database = firebase.database()


class HomePageView(View):

    def get(self, request, *args, **kwargs):
        # post_title = database.child('Post').child('post_title').get().val()
        # post_image = database.child('Post').child('post_image').get().val()
        # post_body = database.child('Post').child('post_body').get().val()
        # post_author = database.child('Post').child('post_author').get().val()
        # post_date = database.child('Post').child('post_date').get().val()

        posts = Post.objects.all()
        reports = Report.objects.all()
        # page = 1
        # result = 3
        # posts_paginator = Paginator(posts, result)
        # reports_paginator = Paginator(reports, result)
        # posts = posts_paginator.page(page)
        # reports = reports_paginator.page(page)
        security_user = User.objects.filter(is_staff=True)
        if request.user in security_user:
            context = {
                'object':security_user,
                'posts':posts,
                'reports':reports,
            }
        else:
            context = {
                'object':'',
                'posts':posts
            }
        return render(request, 'crime/home_page.html', context)


def contact_us(request):
    return render(request, 'crime/contact_us.html', context={'title':'Contact Us'})


class PostListView(ListView):
    model = Post
    ordering = ['-post_date']


class PostDetailView(DetailView):
    model = Post


@login_required
def post_create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post_data = form.save(commit=False)
            post_data.post_author = request.user
            form.save()
            return redirect('post-list')
    return render(request, 'crime/post_form.html', context={'form':form})


class ReportListView(ListView):
    model = Report
    ordering = ['-report_date']


class ReportDetailView(DetailView):
    model = Report


@login_required
def report_create(request):
    form = ReportForm()
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report_data = form.save(commit=False)
            report_data.report_author = request.user
            form.save()
            report_title = form.cleaned_data['report_title']
            messages.warning(request, f'New Crime Report Notification Sent: Titled - {report_title}')
            return redirect('post-list')
    return render(request, 'crime/report_form.html', context={'form':form})


def register(request):
    if request.method == "POST":
        form = RegisterCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}!')
            return redirect('login')
    else:
        form = RegisterCreationForm()
    return render(request, 'crime/register.html', {'form':form})








