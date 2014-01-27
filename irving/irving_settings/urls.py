from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^dashboard/', include('dashboard.urls')),
	url(r'^xhr/', include('dashboard.urls')),
    url(r'^adminarea/', include(admin.site.urls)),
    url(r'^selectchaining/', include('smart_selects.urls')),
	
		# Login / logout.
#    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^login/$', 'login.views.checkLogin'),
	url(r'^extendsession/$', 'login.views.extendSession'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/dashboard/'}, name='auth_logout'),
	url(r'^logout/(?P<next_page>.*)/$', 'django.contrib.auth.views.logout', name='auth_logout_next'),
)	


if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'irving_settings/sitestatic'}),
    )