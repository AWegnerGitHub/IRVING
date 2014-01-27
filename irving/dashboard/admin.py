from dashboard.models import *
from django.contrib import admin
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from models import UserProfile

class DatabaseTypesAdmin(admin.ModelAdmin):
	'''
	This form is used to add new database types (Oracle, DB2, MySQL, etc) to the system
	'''
	fieldsets = [
		(None, {'fields' : ['database_desc', 'is_active']}),
		('Database Details', {'fields' : ['driver_location']}),	
	]
	
	list_display = ('database_desc', 'is_active')
	list_filter = ['is_active']
	ordering = ['-is_active','database_desc']
	
class SystemAdmin(admin.ModelAdmin):
	'''
	This form is used to add new client systems to the system. These are the systems that
	will be queried in the dashboard.
	
	'database_name' needs to be a field that matches a key in settings.DATABASES
	'''
	def formfield_for_foreignkey(self,db_field,request, **kwargs):
		if db_field.name == 'database_type':
			kwargs['queryset'] = DatabaseType.objects.exclude(is_active=False)
		return super(SystemAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

	fieldsets = [
		('Database Information', {'fields' : ['database_type','database_name']}),
		('System Information', {'fields' : ['system_desc','is_active']}),
	]
	
	list_display = ('system_desc','database_type','database_name','is_active')
	ordering = ['database_type','system_desc','is_active']
	list_filter = ['database_type','is_active']
	search_fields = ['system_desc']
	
class SystemGroupAdmin(admin.ModelAdmin):
	'''
	This form links a set of data in a client system to a particular system. This can be used
	to create seperate 'groups' within the same system. IE. Accessing a single install of TM you
	can set groups to be each specific customer within TM
	'''
	fieldsets = [
		(None, {'fields' : ['system']}),
		('Group Information', {'fields' : ['group_desc','cust_cd','division','lgst_grp','is_active']}),		
	]
	
	list_display = ['group_desc','system','lgst_grp','division','cust_cd','is_active']
	ordering = ['group_desc']
	list_filter = ['lgst_grp','division','cust_cd','is_active']
	search_fields = ['lgst_grp','division','cust_cd','group_desc']
	
class QueryDataAdmin(admin.ModelAdmin):
	'''
	This form is where the queries are input in the system, complete with placeholders
	'''
	
	fieldsettxt = """
	<table id="templatetagstxt">
		<tr>
			<th>Template String</th>
			<th>Substituted Value</th>
		</tr>
		<tr>
			<td>&lt;NOW&gt;<br />
				&lt;NOW_TZ&gt;</td>
			<td>The current date and time to the second; adding "_TZ" includes the user's timezone offset offset from UTC</td>
		</tr>
		<tr>
			<td>&lt;TODAYSTART&gt;<br />
				&lt;TODAYSTART_TZ&gt;
				</td>
			<td>The current date at midnight; adding "_TZ" includes the user's timezone offset offset from UTC</td>
		</tr>		
		<tr>
			<td>&lt;TODAYEND&gt;<br />
				&lt;TODAYEND_TZ&gt;
				</td>
			<td>The current date at 23:59:59; adding "_TZ" includes the user's timezone offset offset from UTC</td>
		</tr>		
		<tr>
			<td>&lt;YESTERDAYSTART&gt;<br />
				&lt;YESTERDAYSTART_TZ&gt;
				</td>
			<td>The previous date at midnight; adding "_TZ" includes the user's timezone offset offset from UTC</td>
		</tr>		
		<tr>
			<td>&lt;YESTERDAYEND&gt;<br />
				&lt;YESTERDAYEND_TZ&gt;
				</td>
			<td>The previous date at 23:59:59; adding "_TZ" includes the user's timezone offset offset from UTC</td>
		</tr>
		<tr>
			<td>&lt;TOMORROWSTART&gt;<br />
				&lt;TOMORROWSTART_TZ&gt;
				</td>
			<td>The next date at midnight; adding "_TZ" includes the user's timezone offset offset from UTC</td>
		</tr>		
		<tr>
			<td>&lt;TOMORROWEND&gt;<br />
				&lt;TOMORROWEND_TZ&gt;
				</td>
			<td>The next date at 23:59:59; adding "_TZ" includes the user's timezone offset offset from UTC</td>
		</tr>
		<tr>
			<td>&lt;MONTHSTART&gt;<br />
				&lt;MONTHSTART_TZ&gt;
				</td>
			<td>Current month's first date at midnight; adding "_TZ" includes the user's timezone offset offset from UTC</td>
		</tr>
		<tr>
			<td>&lt;MONTHEND&gt;<br />
				&lt;MONTHEND_TZ&gt;
				</td>
			<td>Current month's last date at 23:59:59; adding "_TZ" includes the user's timezone offset offset from UTC</td>
		</tr>
		<tr>
			<td>&lt;LASTMONTHSTART&gt;<br />
				&lt;LASTMONTHSTART_TZ&gt;
				</td>
			<td>Previous month's first date at midnight; adding "_TZ" includes the user's timezone offset offset from UTC</td>
		</tr>
		<tr>
			<td>&lt;LASTMONTHEND&gt;<br />
				&lt;LASTMONTHEND_TZ&gt;
				</td>
			<td>Previous month's last date at 23:59:59; adding "_TZ" includes the user's timezone offset offset from UTC</td>
		</tr>
		<tr>
			<td>&lt;THISYEARSTART&gt;<br />
				&lt;THISYEARSTART_TZ&gt;
				</td>
			<td>Current year on January 1 at midnight; adding "_TZ" includes the user's timezone offset offset from UTC</td>
		</tr>
		<tr>
			<td>&lt;THISYEAREND&gt;<br />
				&lt;THISYEAREND_TZ&gt;
				</td>
			<td>Current year on Dec 31 at 23:59:59; adding "_TZ" includes the user's timezone offset offset from UTC</td>
		</tr>
		<tr>
			<td>&lt;LASTYEARSTART&gt;<br />
				&lt;LASTYEARSTART_TZ&gt;
				</td>
			<td>Previous year on January 1 at midnight; adding "_TZ" includes the user's timezone offset offset from UTC</td>
		</tr>
		<tr>
			<td>&lt;LASTYEAREND&gt;<br />
				&lt;LASTYEAREND_TZ&gt;
				</td>
			<td>Previous year on Dec 31 at 23:59:59; adding "_TZ" includes the user's timezone offset offset from UTC</td>
		</tr>
		<tr>
			<td>&lt;HIST&gt;</td>
			<td>Value set in the Dashboard group's 'History Days' setting. This setting is generally used to limit the number of days a historical query will go back. Example: Setting a group to show a rolling 7 days of history will show all queries that use this template tag. This value is changeable by end users</td>
		</tr>
		<tr>
			<td>&lt;CUST_CD&gt;</td>
			<td>Customer code that was set in the Customer section and that is associated with this query. A customer code can change for a query if multiple customer groups are defined within a system and the query is used for each group on a user's dashboard</td>
		</tr>
		<tr>
			<td>&lt;DIVISION&gt;</td>
			<td>Division code that was set in the Customer section and that is associated with this query. A division code can change for a query if multiple customer groups are defined within a system and the query is used for each group on a user's dashboard</td>
		</tr>
		<tr>
			<td>&lt;LGST_GRP&gt;</td>
			<td>Logistics code that was set in the Customer section and that is associated with this query. A logistics code can change for a query if multiple customer groups are defined within a system and the query is used for each group on a user's dashboard</td>
		</tr>
	</table>
	"""
	
	fieldsets = [
		(None, {'fields' : ['system']}),
		('Query Information', {'fields' : ['qry_desc','qry_txt','is_active','is_errorpanelquery','errorpanel_disp_order']}),		
		('Query Replacement Strings', {'classes': ('collapse',), 'fields' : [], 'description':fieldsettxt}),
	]
	list_display = ['qry_desc','system','is_active']
	list_filter = ['system','is_active']
	ordering = ['system','qry_desc']
	search_fields = ['qry_desc']

class UserDashboardGroupInLine(admin.TabularInline):
	'''
	This form allows inline editting of dashboard groups
	'''
	model = UserDashboardGroup
	exclude = ['user']
	extra = 0
	ordering = ['disp_order']
	
class UserGroupQueryInLine(admin.TabularInline):
	'''
	This form allows inline editting of queries in dashboard groups
	'''
	model = UserGroupQuery	
	exclude = ['user']
	extra = 0
	
	def queryset(self, request):
		# Redefining queryset to filter results down to user only
		user = getattr(request, 'user', None)
		qs = super(UserGroupQueryInLine, self).queryset(request)
		return qs.filter(user=user)	
		
	def formfield_for_foreignkey(self,db_field,request, **kwargs):
		user = getattr(request, 'user', None)
		
		dashboard_id = request.path_info.split("/")[-2]
		
		if db_field.name == 'user':
			kwargs['initial'] = request.user
		if db_field.name == 'dashboard':
			kwargs['queryset'] = UserDashboard.objects.exclude(~Q(user=user))
		try:			# Needed if no dashboard is defined
			if db_field.name == 'user_dashboard_group':
				kwargs['queryset'] = UserDashboardGroup.objects.exclude(~Q(user=user)).filter(dashboard=dashboard_id)
		except:
			pass
		return super(UserGroupQueryInLine, self).formfield_for_foreignkey(db_field, request, **kwargs)		
		
	ordering = ['user_dashboard_group','disp_order']
	

	
class UserDashboardAdmin(admin.ModelAdmin):
	'''
	This form allows a user to create a new dashboard
	'''
	def queryset(self, request):
		# Redefining queryset to filter results down to user only
		user = getattr(request, 'user', None)
		qs = super(UserDashboardAdmin, self).queryset(request)
		return qs.filter(user=user)

	def has_delete_permission(self, request, obj=None):   
		user = getattr(request, 'user', None)
		if not obj:
			return False
		return super(UserDashboardAdmin, self).has_delete_permission(request, obj)

	def has_change_permission(self, request, obj=None):   
		user = getattr(request, 'user', None)
		if not obj:
			return True
		return super(UserDashboardAdmin, self).has_change_permission(request, obj)

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()
		
	fieldsets = [
		(None, {'fields' : ['board_name', 'refresh_interval']}),
	]
	
	inlines = [UserDashboardGroupInLine,UserGroupQueryInLine]
	list_display = ['board_name', 'refresh_interval']
	ordering = ['board_name']
	search_fields = ['board_name']
	actions = None


	# Show our user profiles
admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInline, ]

admin.site.register(User, UserProfileAdmin)

	

# Remove the admin Site models
from django.contrib.sites.models import Site
admin.site.unregister(Site)
	
	
# Finally, register all of the above models
admin.site.register(DatabaseType, DatabaseTypesAdmin)
admin.site.register(System, SystemAdmin)
admin.site.register(SystemGroup,SystemGroupAdmin)
admin.site.register(QueryData, QueryDataAdmin)
admin.site.register(UserDashboard, UserDashboardAdmin)