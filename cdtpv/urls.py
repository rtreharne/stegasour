from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'cdtpv.views.home', name='home'),
    url(r'^handbook/$', 'cdtpv.views.handbook', name='handbook'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('profiles.urls')),
    url(r'^training/', include('training.urls')),
    url(r'^directory/researchers/', 'cdtpv.views.researchers', name='researchers'),
    url(r'^directory/academics/', 'cdtpv.views.academics', name='academics'),
)

if settings.DEBUG:
	urlpatterns += patterns(
			'django.views.static',
			(r'^media/(?P<path>.*)',
			'serve',
			{'document_root': settings.MEDIA_ROOT}),
                        )
