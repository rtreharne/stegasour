from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^core-level/$', 'training.views.core_level_training', name='core-level'),
    url(r'^core-level/(?P<module_id>\d+)/$', 'training.views.core_module', name='core-module'),
    url(r'^submission/(?P<module_id>\d+)/(?P<assessment_id>\d+)/$', 'training.views.submit_assessment', name='submit-assessment'),
	
)
