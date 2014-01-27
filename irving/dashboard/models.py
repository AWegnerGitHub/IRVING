from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
from django.db.models.signals import post_save

class PositiveIntegerRangeField(models.PositiveIntegerField):
	'''
	Set up a valid range of values for a Positive Integer Field
	'''
	def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
		self.min_value, self.max_value = min_value, max_value
		models.IntegerField.__init__(self, verbose_name, name, **kwargs)
	
	def formfield(self, **kwargs):
		defaults = {'min_value': self.min_value, 'max_value':self.max_value}
		defaults.update(kwargs)
		return super(PositiveIntegerRangeField, self).formfield(**defaults)

class DatabaseType(models.Model):
	allow_sync = True
	database_desc = models.CharField(max_length=25)
	driver_location = models.CharField(max_length=300, null=True, blank=True)
	is_active = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.database_desc
		
	class Meta:
		verbose_name = u'Database Backend'
		verbose_name_plural = u'Database Backends'
		
class System(models.Model):
	allow_sync = True
	system_desc = models.CharField('System Name', max_length=50)
	database_name = models.CharField('Django Database Name', max_length=25)
	is_active = models.BooleanField(default=True)
	database_type = models.ForeignKey(DatabaseType)
	
	def __unicode__(self):
		return self.system_desc
		
	class Meta:
		verbose_name = u'System'
		verbose_name_plural = u'Systems'
	
class SystemGroup(models.Model):
	allow_sync = True
	group_desc = models.CharField('Group Name',max_length=25)
	cust_cd = models.CharField('Customer Code',max_length=25, null=True, blank=True)
	division = models.CharField('Division Code',max_length=25, null=True, blank=True)
	lgst_grp = models.CharField('Logistics Group',max_length=25, null=True, blank=True)
	is_active = models.BooleanField(default=True)
	system = models.ForeignKey(System)
	
	def __unicode__(self):
		return self.group_desc
		
	class Meta:
		verbose_name = u'Customer'
		verbose_name_plural = u'Customers'
	
class QueryData(models.Model):
	allow_sync = True
	qry_desc = models.CharField('Query Description', max_length=50)
	qry_txt = models.TextField(max_length=2000)
	is_active = models.BooleanField(default=True)
	system = models.ForeignKey(System)
	is_errorpanelquery = models.BooleanField('Is Query for Error panel',default=False)
	errorpanel_disp_order = models.PositiveSmallIntegerField('Display order in Error Panel')
	
	def __unicode__(self):
		return self.qry_desc

	class Meta:
		verbose_name = u'Query'
		verbose_name_plural = u'Queries'
	
class UserDashboard(models.Model):
	allow_sync = True
	user = models.ForeignKey(User)
	board_name = models.CharField('Dashboard Name', max_length=50)
	refresh_interval = PositiveIntegerRangeField(default=60, min_value=1, max_value=480)		# Minimium of 1 minute, max of 8 hours
	
	def __unicode__(self):
		return self.board_name

	class Meta:
		verbose_name = u'Dashboard'
		verbose_name_plural = u'Dashboards'

class UserDashboardGroup(models.Model):
	allow_sync = True
	group_desc = models.CharField('Group Display Title', max_length=50)
	user = models.ForeignKey(User)
	dashboard = models.ForeignKey(UserDashboard)
	system = models.ForeignKey(System)
	system_group = ChainedForeignKey(SystemGroup, chained_field='system', chained_model_field='system')
	history_days = models.PositiveIntegerField(default=30)
	disp_order = models.PositiveSmallIntegerField()
	
	def __unicode__(self):
		return self.group_desc

	def save(self, *args, **kwargs):
		self.user = self.dashboard.user
		super(UserDashboardGroup,self).save(*args, **kwargs)
		
	class Meta:
		verbose_name = u'Dashboard Group'
		verbose_name_plural = u'Dashboard Groups'

class UserGroupQuery(models.Model):
	allow_sync = True
	user = models.ForeignKey(User)
	dashboard = ChainedForeignKey(UserDashboard, chained_field='user', chained_model_field='user', show_all=False, auto_choose=True)
	user_dashboard_group = models.ForeignKey(UserDashboardGroup)
	system = ChainedForeignKey(System, chained_field='user_dashboard_group', chained_model_field='userdashboardgroup', auto_choose=True)
	query = ChainedForeignKey(QueryData, chained_field='system', chained_model_field='system')
	
	#	query = models.ForeignKey(QueryData)
	warning_threshold = models.IntegerField(default=0)
	fatal_threshold = models.IntegerField(default=0)
	disp_order = models.PositiveSmallIntegerField()
	
	def __unicode__(self):
		return self.user_dashboard_group.group_desc
		
	def save(self, *args, **kwargs):
		self.user = self.dashboard.user
		super(UserGroupQuery,self).save(*args, **kwargs)

	class Meta:
		verbose_name = u'Dashboard Group Query'
		verbose_name_plural = u'Dashboard Group Queries'
		
		
class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True)
	is_displayonly = models.BooleanField('Display Only User', default=False)
	last_board = models.ForeignKey(UserDashboard, null=True, blank=True)
	warning_color = models.CharField('Warning Display Color', max_length=7, null=True, blank=True)
	fatal_color = models.CharField('Error Display Color', max_length=7, null=True, blank=True)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

