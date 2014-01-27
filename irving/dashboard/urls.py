from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView

urlpatterns = patterns('',
	url(r'^$','dashboard.views.dashboard'),	
	(r'^(?P<dashboard_id>\d+)$', 'dashboard.views.dashboard'),
	(r'^runquery/$','dashboard.views.xhr_runqueries'),
	(r'^boardorder/$','dashboard.views.xhr_boardorder'),
	(r'^detaildata/(?P<id>\d+)$', 'dashboard.views.xhr_runquery'),
	(r'^errordata/(?P<id>\d+)$', 'dashboard.views.xhr_runerrquery'),
	(r'^changepass/$', 'dashboard.views.xhr_changepassword'),
)