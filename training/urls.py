from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^core-level/$', 'training.views.core_level_training', name='core-level'),
	
)
