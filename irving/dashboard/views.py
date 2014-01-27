from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.utils import simplejson
from django.conf import settings
from models import *
from functions import Query
from django.db import connections, DatabaseError, IntegrityError
from django.contrib.humanize.templatetags.humanize import intcomma
from django.contrib.auth.models import User
import cx_Oracle
import MySQLdb
import django.db.backends.oracle.base, django.db.backends.mysql.base, sqlserver_ado.base
from django.http import Http404
import sys

from collections import OrderedDict


def dashboard(request, dashboard_id=None):
	'''
	Base view for the dashboard
	'''
	error_str = None
	is_error = False
	dashboards = []
	active_dashboard = None
	
		# Gather current dashboard
	if dashboard_id:
		try:
			active_dashboard = UserDashboard.objects.filter(user=request.user.id, id=dashboard_id)[0]
			request.user.get_profile().last_board = active_dashboard
			request.user.get_profile().save()
		except IndexError:							# Someone is trying to access a dashboard they don't own, give them their first one instead
			active_dashboard = UserDashboard.objects.filter(user=request.user.id)[0]
			error_str = "Invalid Dashboard Selection. Displaying default dashboard."
			is_error = True 
	else:
		try:
			active_dashboard = UserDashboard.objects.filter(id=request.user.get_profile().last_board.id)[0]
		except:
			try:
				active_dashboard = UserDashboard.objects.filter(user=request.user.id)[0]
				request.user.get_profile().last_board = active_dashboard
				request.user.get_profile().save()
			except:
				pass
		# Gather current groups
	groups = UserDashboardGroup.objects.filter(dashboard=active_dashboard).order_by('disp_order')
	
		# Put the queries in the groups
	dashboard_groups = OrderedDict()
	for group in groups:
		dashboard_groups[group] = UserGroupQuery.objects.filter(user_dashboard_group=group).order_by('disp_order')
		
	errorpanel = OrderedDict()
	errorpanel = QueryData.objects.filter(is_errorpanelquery=True).order_by('errorpanel_disp_order')

		# List all dashboards
	dashboards = UserDashboard.objects.filter(user=request.user.id)
	if active_dashboard:
		curDash = active_dashboard
	else:
		curDash = {'refresh_interval':60}
	return render_to_response('dashboard/main.html', {'dashboards': dashboards, 'currentDash': curDash, 'errorStr': error_str, 'isError': is_error, 'dashboardGroups': dashboard_groups, 'errorqueries': errorpanel, 'session_len' : settings.SESSION_EXPIRE_TIME, 'session_poll_time' : settings.SESSION_EXPIRE_TIME / 10},
                               context_instance=RequestContext(request))
	
def xhr_runqueries(request):
	'''
	Runs the queries for the dashboard to display
	'''
	response_dict = {'success' : False}
	if request.is_ajax() or settings.DEBUG:
		if request.method == u'GET':
			GET = request.GET
			if GET.has_key(u'ugq_id') and GET.has_key(u'res_span'):
				ugq_id = int(GET[u'ugq_id'].split('_')[-1])
				response_dict['ugq_id'] = ugq_id
				response_dict['res_span'] = GET[u'res_span']
				data = UserGroupQuery.objects.filter(id=response_dict['ugq_id'])[0]
				query_id = data.query_id
				query = QueryData.objects.filter(id=data.query_id)[0].qry_txt
				response_dict['warning_threshold'] = data.warning_threshold
				response_dict['fatal_threshold'] = data.fatal_threshold
				system = data.system.id
				system_db = data.system.database_name
				system_active = data.system.is_active
				sysgroup = SystemGroup.objects.filter(id=data.user_dashboard_group.system_group_id)[0]
				
				hist = data.user_dashboard_group.history_days
				cust_cd = sysgroup.cust_cd
				division = sysgroup.division
				lgst_grp = sysgroup.lgst_grp

				# Next - query 'Query' object, passing in the 'query' and all kwargs, return a query string
				args = {'<CUST_CD>': cust_cd,
						'<DIVISION>': division,
						'<LGST_GRP>': lgst_grp,
						'<HIST>': hist,
				}
				querydata = Query(qrystr=query, **args)
				query = querydata.QueryString
					# Start Query
				try:
					myCursor = connections[system_db].cursor()
					results = myCursor.execute(query)
					
					print type(connections[system_db])
					
					if type(connections[system_db]) == django.db.backends.oracle.base.DatabaseWrapper:
						resultcount = results.fetchall()
						response_dict['resultsetcount'] = intcomma(len(resultcount))
						response_dict['resultsetcmp'] = len(resultcount)
						response_dict['success'] = True 
					elif type(connections[system_db]) == django.db.backends.mysql.base.DatabaseWrapper:
						resultcount = myCursor.fetchall()
						response_dict['resultsetcount'] = intcomma(len(resultcount))
						response_dict['resultsetcmp'] = len(resultcount)
						response_dict['success'] = True 
					elif type(connections[system_db]) == sqlserver_ado.base.DatabaseWrapper:
						resultcount = myCursor.fetchall()
						response_dict['resultsetcount'] = intcomma(len(resultcount))
						response_dict['resultsetcmp'] = len(resultcount)
						response_dict['success'] = True 
					else:
						print "None selected"
				except (cx_Oracle.DatabaseError, DatabaseError, MySQLdb.OperationalError) as e:
					response_dict['resultsetcount'] = 0	
					
			# Error panel queries
			elif GET.has_key(u'qry_id') and GET.has_key(u'res_span'):
				qry_id = int(GET[u'qry_id'].split('_')[-1])
				response_dict['qry_id'] = qry_id
				response_dict['res_span'] = GET[u'res_span']
				query_id = qry_id
				query = QueryData.objects.filter(id=query_id)[0].qry_txt
				response_dict['warning_threshold'] = 0
				response_dict['fatal_threshold'] = 1
				system = QueryData.objects.filter(id=query_id)[0].system_id
				system_db = QueryData.objects.filter(id=query_id)[0].system.database_name
				system_active = QueryData.objects.filter(id=query_id)[0].system.is_active
				args = {}
				
				querydata = Query(qrystr=query, **args)
				query = querydata.QueryString
				response_dict['query'] = query
				
					# Start Query
				try:
					myCursor = connections[system_db].cursor()
					results = myCursor.execute(query)
					
					if type(connections[system_db]) == django.db.backends.oracle.base.DatabaseWrapper:
						resultcount = results.fetchall()
						response_dict['resultsetcount'] = intcomma(len(resultcount))
						response_dict['resultsetcmp'] = len(resultcount)
						response_dict['success'] = True 
					elif type(connections[system_db]) == django.db.backends.mysql.base.DatabaseWrapper:
						resultcount = myCursor.fetchall()
						response_dict['resultsetcount'] = intcomma(len(resultcount))
						response_dict['resultsetcmp'] = len(resultcount)
						response_dict['success'] = True 
					elif type(connections[system_db]) == sqlserver_ado.base.DatabaseWrapper:
						resultcount = myCursor.fetchall()
						response_dict['resultsetcount'] = intcomma(len(resultcount))
						response_dict['resultsetcmp'] = len(resultcount)
						response_dict['success'] = True 
					else:
						print "None selected"
				except (cx_Oracle.DatabaseError, DatabaseError, MySQLdb.OperationalError) as e:
					response_dict['resultsetcount'] = 0	
		else:
			raise Http404
	else:
		raise Http404

	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/json')
	
	
def xhr_boardorder(request):
	'''
	Used to change groupings within a dashboard when groups are drag/dropped
	'''
	response_dict = {'success' : False}
	
	if request.is_ajax() or settings.DEBUG:
		if request.method == u'GET':
			GET = request.GET
			if GET.has_key(u'currentOrder'):
				orderarray = GET[u'currentOrder'].split(',')
				orderval = 1
				try:
					for group in orderarray:
						curgroup = group.split('_')[-1]
						p = get_object_or_404(UserDashboardGroup, id=curgroup)
						p.disp_order = orderval
						orderval = orderval + 1
						p.save()
					response_dict['success'] = True
				except:
					pass
			elif GET.has_key(u'currentErrOrder'):
				orderarray = GET[u'currentErrOrder'].split(',')
				orderval = 1
				try:
					for group in orderarray:
						curgroup = group.split('_')[-1]
						p = get_object_or_404(QueryData, id=curgroup)
						p.errorpanel_disp_order = orderval
						orderval = orderval + 1
						p.save()
					response_dict['success'] = True
				except:
					pass
			elif GET.has_key(u'currentQryOrder'):
				orderarray = GET[u'currentQryOrder'].split(',')
				orderval = 1
				try:
					for group in orderarray:
						curgroup = group.split('_')[-1]
						p = get_object_or_404(UserGroupQuery, id=curgroup)
						p.disp_order = orderval
						orderval = orderval + 1
						p.save()
					response_dict['success'] = True
				except:
					pass
	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/json')

def xhr_runquery(request, id=None):
	'''
	Runs the queries for the dashboard to display
	'''
	response_dict = {'success' : False}
	response_dict['ugq_id'] = int(id)
	data = UserGroupQuery.objects.filter(id=response_dict['ugq_id'])[0]
	query_id = data.query_id
	query = QueryData.objects.filter(id=data.query_id)[0].qry_txt
	response_dict['query_desc'] = QueryData.objects.filter(id=data.query_id)[0].qry_desc
	response_dict['warning_threshold'] = data.warning_threshold
	response_dict['fatal_threshold'] = data.fatal_threshold
	system = data.system.id
	system_db = data.system.database_name
	system_active = data.system.is_active
	sysgroup = SystemGroup.objects.filter(id=data.user_dashboard_group.system_group_id)[0]
	
	hist = data.user_dashboard_group.history_days
	cust_cd = sysgroup.cust_cd
	division = sysgroup.division
	lgst_grp = sysgroup.lgst_grp

	# Next - query 'Query' object, passing in the 'query' and all kwargs, return a query string
	args = {'<CUST_CD>': cust_cd,
			'<DIVISION>': division,
			'<LGST_GRP>': lgst_grp,
			'<HIST>': hist,
	}
	querydata = Query(qrystr=query, **args)
	query = querydata.QueryString
	response_dict['params'] = args

	if is_dashsuperuser(request.user) or is_dashadmin(request.user):
		response_dict['query'] = query
		
		# Start Query
	try:
		myCursor = connections[system_db].cursor()
		results = myCursor.execute(query)
		
		if type(connections[system_db]) == django.db.backends.oracle.base.DatabaseWrapper:
			resultcount = results.fetchall()
			response_dict['resultsetcount'] = intcomma(len(resultcount))
			response_dict['resultset'] = resultcount
			response_dict['cols'] = [d[0] for d in results.description] 
			response_dict['success'] = True 
		elif type(connections[system_db]) == django.db.backends.mysql.base.DatabaseWrapper:
			resultcount = myCursor.fetchall()
			response_dict['resultsetcount'] = intcomma(len(resultcount))
			response_dict['resultset'] = resultcount
			response_dict['cols'] = [d[0] for d in myCursor.description] 
			response_dict['success'] = True 
		elif type(connections[system_db]) == sqlserver_ado.base.DatabaseWrapper:
			resultcount = myCursor.fetchall()
			response_dict['resultsetcount'] = intcomma(len(resultcount))
			response_dict['resultset'] = resultcount
			response_dict['cols'] = [d[0] for d in myCursor.description] 
			response_dict['success'] = True 
		else:
			print "None selected"
	except (cx_Oracle.DatabaseError, DatabaseError, MySQLdb.OperationalError) as e:
		response_dict['resultsetcount'] = 0	
		if is_dashsuperuser(request.user) or is_dashadmin(request.user):
			response_dict['errorMsg'] = "Error while executing query:\nError message: {0}".format(e)
#	except:
#		print "Unexpected error:", sys.exc_info()

	return render_to_response('dashboard/querydetails.html', {'results': response_dict}, context_instance=RequestContext(request))


def xhr_runerrquery(request, id=None):
	'''
	Runs the queries from the error panel for the dashboard to display
	'''
	response_dict = {'success' : False}
	
	response_dict['qry_id'] = int(id)
	query_id = int(id)
	query = QueryData.objects.filter(id=query_id)[0].qry_txt
	response_dict['query_desc'] = QueryData.objects.filter(id=query_id)[0].qry_desc
	response_dict['warning_threshold'] = 0
	response_dict['fatal_threshold'] = 1
	system = QueryData.objects.filter(id=query_id)[0].system_id
	system_db = QueryData.objects.filter(id=query_id)[0].system.database_name
	system_active = QueryData.objects.filter(id=query_id)[0].system.is_active
	args = {}
	response_dict['params'] = args
	querydata = Query(qrystr=query, **args)
	query = querydata.QueryString
	if is_dashsuperuser(request.user) or is_dashadmin(request.user):
		response_dict['query'] = query
	
		# Start Query
	try:
		myCursor = connections[system_db].cursor()
		results = myCursor.execute(query)
		
		if type(connections[system_db]) == django.db.backends.oracle.base.DatabaseWrapper:
			resultcount = results.fetchall()
			response_dict['resultsetcount'] = intcomma(len(resultcount))
			response_dict['resultset'] = resultcount
			response_dict['cols'] = [d[0] for d in results.description] 
			response_dict['success'] = True 
		elif type(connections[system_db]) == django.db.backends.mysql.base.DatabaseWrapper:
			resultcount = myCursor.fetchall()
			response_dict['resultsetcount'] = intcomma(len(resultcount))
			response_dict['resultset'] = resultcount
			response_dict['cols'] = [d[0] for d in myCursor.description] 
			response_dict['success'] = True 
		elif type(connections[system_db]) == sqlserver_ado.base.DatabaseWrapper:
			resultcount = myCursor.fetchall()
			response_dict['resultsetcount'] = intcomma(len(resultcount))
			response_dict['resultset'] = resultcount
			response_dict['cols'] = [d[0] for d in myCursor.description] 
			response_dict['success'] = True 
		else:
			print "None selected"
	except (cx_Oracle.DatabaseError, DatabaseError, MySQLdb.OperationalError) as e:
		response_dict['resultsetcount'] = 0	
		if is_dashsuperuser(request.user) or is_dashadmin(request.user):
			response_dict['errorMsg'] = "Error while executing query:\nError message: {0}".format(e)		

	return render_to_response('dashboard/querydetails.html', {'results': response_dict}, context_instance=RequestContext(request))

def xhr_changepassword(request):
	'''
	Used to change a user's password
	'''
	response_dict = {'success' : False}
	
	user = getattr(request, 'user', None)
	if request.is_ajax() or settings.DEBUG:
		if request.method == u'POST':
			POST = request.POST
			# Check old pass
			if user.check_password(POST['oldpass']):
				user.set_password(POST['newpass'])
				user.save()
				response_dict['success'] = True
			else:
				response_dict['errormsg'] = "Old Password is incorrect"

	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/json')
			
def is_dashsuperuser(user):
	'''
	Checks if a user has the Dashboard Super User permission
	'''
	if user:
		return user.groups.filter(name='Dashboard Super User').count() == 1
	return False
	
def is_dashadmin(user):
	'''
	Checks if a user has the Dashboard Super User permission
	'''
	if user:
		return user.groups.filter(name='Dashboard Admin').count() == 1
	return False
