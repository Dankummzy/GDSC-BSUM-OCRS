import requests
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import Post, Report
from .forms import RegisterCreationForm, PostForm, ReportForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import pyrebase
from django.core.files.storage import default_storage
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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
storage = firebase.storage()


class HomePageView(View):

    def get(self, request, *args, **kwargs):

        posts = Post.objects.all()
        reports = Report.objects.all()

        posts_paginator = Paginator(posts, 3)
        posts_page_number = request.GET.get('page')
        posts_page_obj = posts_paginator.get_page(posts_page_number)

        reports_paginator = Paginator(reports, 3)
        reports_page_number = request.GET.get('page')
        reports_page_obj = reports_paginator.get_page(reports_page_number)

        security_user = User.objects.filter(is_staff=True)
        if request.user in security_user:
            context = {
                'object':security_user,
                'posts':posts,
                'reports':reports,
                'posts_page_obj':posts_page_obj,
                'reports_page_obj':reports_page_obj

            }
        else:
            context = {
                'object':'',
                'posts':posts,
                'posts_page_obj': posts_page_obj,
            }
        return render(request, 'crime/home_page.html', context)


def contact_us(request):
    return render(request, 'crime/contact_us.html', context={'title':'Contact Us'})


class PostListView(ListView):
    model = Post
    paginate_by = 3
    ordering = ['-post_date']


class PostDetailView(DetailView):
    model = Post


@login_required
def post_create(request):
    storage.child()
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post_image = request.FILES['post_image']
            file_save = default_storage.save(post_image.name, post_image)
            storage.child("files/" + post_image.name).put("media/" + post_image.name)
            delete = default_storage.delete(post_image.name)
            post_data = form.save(commit=False)
            post_data.post_author = request.user
            form.save()
            return redirect('post-list')
    return render(request, 'crime/post_form.html', context={'form':form})


class ReportListView(ListView):
    model = Report
    paginate_by = 3
    ordering = ['-report_date']


class ReportDetailView(DetailView):
    model = Report


@login_required
def report_create(request):
    form = ReportForm()
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report_image = request.FILES['report_image']
            file_save = default_storage.save(report_image.name, report_image)
            storage.child("files/" + report_image.name).put("media/" + report_image.name)
            delete = default_storage.delete(report_image.name)
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








