from django.urls import path
from .views import (PostListView, PostDetailView, ReportListView, ReportDetailView,
                    report_create, HomePageView, contact_us, register, post_create, signIn, postsignIn, logOut)


urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('contact-us/', contact_us, name='contact-us'),
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create/new/', post_create, name='post-create'),
    path('report/', ReportListView.as_view(), name='report-list'),
    path('report/detail/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('report/create/new/', report_create, name='report-create'),
    path('register/', register, name='register'),
    path('login/', signIn, name='login'),
    path('postsignIn/', postsignIn, name='post-login'),
    path('logout/', logOut, name='logout'),
]