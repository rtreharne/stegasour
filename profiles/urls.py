from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^dashboard/$', 'profiles.views.dashboard', name='dashboard'),
    url(r'login/$', 'profiles.views.user_login', name='login'),
    url(r'logout/$', 'profiles.views.user_logout', name='logout'),
)
