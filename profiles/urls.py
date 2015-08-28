from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^dashboard/$', 'profiles.views.dashboard', name='dashboard'),
    url(r'login/$', 'profiles.views.user_login', name='login'),
    url(r'logout/$', 'profiles.views.user_logout', name='logout'),
    url(r'^update_profile/$', 'profiles.views.update_profile', name='update_profile'),
    url(r'^update_project/$', 'profiles.views.update_project', name='update_project'),
    url(r'^add_portfolio_item/$', 'profiles.views.add_portfolio_item', name='add_portfolio_item'),
    url(r'^delete_portfolio_item/(?P<upload_id>\d+)/$', 'profiles.views.delete_portfolio_item', name='delete__portfolio_item')
	
)
