from django.contrib.auth import logout
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.conf import settings

def checkLogin(request, *args, **kwargs):
	'''
	Forces user to log in before continuing
	'''
	if request.user.is_authenticated():
		return HttpResponseRedirect('/dashboard/')
	else:
		return login(request)
		
def extendSession(request):
	'''
	Extends session
	'''
	response_dict = {'success' : False}
	
	if request.is_ajax() or settings.DEBUG:
		request.session.set_expiry(settings.SESSION_EXPIRE_TIME)
		response_dict['success'] = True 
	else:
		request.session.set_expiry(1)		# Expire in 1 second
		response_dict['success'] = False
	
	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/json')