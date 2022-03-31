from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_image = models.ImageField(upload_to='media/post/', blank=True, null=True)
    post_slug = models.SlugField()
    post_body = RichTextField(default='Write some text here')
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Report(models.Model):

    report_title = models.CharField(max_length=100)
    report_image = models.ImageField(upload_to='media/report/', blank=True, null=True)
    report_body = RichTextField(default='Write some text here')
    report_location = models.CharField(max_length=50)
    report_author = models.ForeignKey(User, on_delete=models.CASCADE)
    report_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.report_title

    def get_absolute_url(self):
        return reverse('report-detail', kwargs={'pk': self.pk })


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_username = models.CharField(max_length=30)
    student_image = models.ImageField(upload_to='media/student/')
    student_email = models.EmailField(default='student@gmail.com')
    student_mat_no = models.CharField(max_length=20)
    student_phone_no = models.CharField(default="+234", max_length=15)

    def __str__(self):
        return self.student_username


class Security(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    security_username = models.CharField(max_length=30)
    security_image = models.ImageField(upload_to='media/security')
    security_email = models.EmailField(default='security@gmail.com')
    security_phone_no = models.CharField(max_length=14, default='+234')

    def __str__(self):
        return self.security_username




