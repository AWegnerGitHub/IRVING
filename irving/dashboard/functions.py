# Common Utilities used by the dashboard

from django.conf import settings
from datetime import datetime, timedelta
import pytz

def TemplateKeysDict():
	templatesDict = {
		'<NOW>': 'now_notz',			
		'<TODAYSTART>': 'todaystart_notz',
		'<TODAYEND>': 'todayend_notz',		
		'<YESTERDAYSTART>': 'yesterdaystart_notz',
		'<YESTERDAYEND>': 'yesterdayend_notz',	
		'<TOMORROWSTART>': 'tomorrowstart_notz',	
		'<TOMORROWEND>':	'tomorrowend_notz',
		'<MONTHSTART>': 'monthstart_notz',
		'<MONTHEND>': 'monthend_notz',
		'<LASTMONTHSTART>': 'lastmonthstart_notz',
		'<LASTMONTHEND>':	'lastmonthstart_notz',
		'<THISYEARBEGIN>': 'yearstart_notz',
		'<THISYEAREND>':	'yearend_notz',
		'<LASTYEARSTART>': 'lastyearstart_notz',	
		'<LASTYEAREND>':	'lastyearend_notz',
		'<NOW_TZ>': 'now_tz',			
		'<TODAYSTART_TZ>': 'todaystart_tz',
		'<TODAYEND_TZ>': 'todayend_tz',		
		'<YESTERDAYSTART_TZ>': 'yesterdaystart_tz',
		'<YESTERDAYEND_TZ>': 'yesterdayend_tz',	
		'<TOMORROWSTART_TZ>': 'tomorrowstart_tz',	
		'<TOMORROWEND_TZ>':	'tomorrowend_tz',
		'<MONTHSTART_TZ>': 'monthstart_tz',
		'<MONTHEND_TZ>': 'monthend_tz',
		'<LASTMONTHSTART_TZ>': 'lastmonthstart_tz',
		'<LASTMONTHEND_TZ>':	'lastmonthstart_tz',
		'<THISYEARBEGIN_TZ>': 'yearstart_tz',
		'<THISYEAREND_TZ>':	'yearend_tz',
		'<LASTYEARSTART_TZ>': 'lastyearstart_tz',	
		'<LASTYEAREND_TZ>':	'lastyearend_tz',

		'<HIST>':	'hist',	
		'<CUST_CD>': 'custcd',	
		'<DIVISION>':	'division',	
		'<LGST_GRP>':	'lgstgrp',	
#		'<SHPM_NUM>': 'shpmnum',				# Not yet used (passed)
#		'<LD_NUM>': 'ldnum',					# Not yet used (passed)
	}
		
	return templatesDict

class Query(object):
	"""
	A class that is used to build a query string used in the dashboard
	"""

	def __init__(self,qrystr=None,**kargs):
		self.QueryString = qrystr
		self.tz = pytz.timezone(settings.TIME_ZONE)
		self.templateDict = {}
		
		if '<HIST>' in kargs:
			self.templateDict['hist'] = kargs['<HIST>']
		else:
			self.templateDict['hist'] = None
		if '<CUST_CD>' in kargs:
			self.templateDict['custcd'] = kargs['<CUST_CD>']
		else:
			self.templateDict['custcd'] = None
		if '<DIVISION>' in kargs:
			self.templateDict['division'] = kargs['<DIVISION>']
		else:
			self.templateDict['division'] = None			
		if '<LD_NUM>' in kargs:
			self.templateDict['ldnum'] = kargs['<LD_NUM>']
		else:
			self.templateDict['ldnum'] = None			
		if '<LGST_GRP>' in kargs:
			self.templateDict['lgstgrp'] = kargs['<LGST_GRP>']
		else:
			self.templateDict['lgstgrp'] = None			
		if '<SHPM_NUM>' in kargs:
			self.templateDict['shpmnum'] = kargs['<SHPM_NUM>']
		else:
			self.templateDict['shpmnum'] = None
		
			
		self.setPlaceHolderValues()
		self.replacePlaceHolders()
		
	def setPlaceHolderValues(self):
		"""
		Replaces the placeholders users put in the queries with actual values
		
		Current template variables are:
			<NOW[_TZ]>				- Current date time [with timezone]
			<TODAYSTART[_TZ]>		- Today at Midnight [with timezone]
			<TODAYEND[_TZ]>			- Today at 23:59:59 [with timezone]
			<YESTERDAYSTART[_TZ]>	- Yesterday at Midnight [with timezone]
			<YESTERDAYEND[_TZ]>		- Yesterday at 23:59:59 [with timezone]
			<TOMORROWSTART[_TZ]>	- Tomorrow at Midnight [with timezone]
			<TOMORROWEND[_TZ]>		- Tomorrow at 23:59:59 [with timezone]
			<MONTHSTART[_TZ]>		- Current month's first day at midnight [with timezone]
			<MONTHEND[_TZ]>			- Current month's last day at 23:59:59 [with timezone]
			<LASTMONTHSTART[_TZ]>	- Last month's first day at midnight [with timezone]
			<LASTMONTHEND[_TZ]>		- Last month's last day at 23:59:59 [with timezone]
			<THISYEARBEGIN[_TZ]>	- Current year Jan 1 at midnight [with timezone]
			<THISYEAREND[_TZ]>		- Current year Dec 31 at 23:59:59 [with timezone]
			<LASTYEARSTART[_TZ]>	- Last year Jan 1 at midnight [with timezone]
			<LASTYEAREND[_TZ]>		- Last year Dec 32 at 23:59:59 [with timezone]
			<HIST>					- History_days in user_dashboard_groups
			<CUST_CD>				- Customer Code set in System_groups for this query
			<DIVISION>				- Division Code set in System_groups for this query
			<LD_NUM>				- Load Number
			<LGST_GRP>				- Logistics Group
			<SHPM_NUM>				- Shipment Number

		"""
		
		# Set up data values
		self.templateDict['now_tz'] = datetime.now(self.tz)
		self.templateDict['todaystart_tz'] = self.tz.localize(self.templateDict['now_tz'].replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None), is_dst=None).astimezone(self.tz)
		self.templateDict['todayend_tz'] = self.tz.localize(self.templateDict['now_tz'].replace(hour=23, minute=59, second=59, microsecond=999999, tzinfo=None), is_dst=None).astimezone(self.tz)
		self.templateDict['yesterdaystart_tz'] = self.tz.localize(self.templateDict['now_tz'].replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None) - timedelta(days=1), is_dst=None).astimezone(self.tz)
		self.templateDict['yesterdayend_tz'] = self.tz.localize(self.templateDict['now_tz'].replace(hour=23, minute=59, second=59, microsecond=999999, tzinfo=None) - timedelta(days=1), is_dst=None).astimezone(self.tz)
		self.templateDict['tomorrowstart_tz'] = self.tz.localize(self.templateDict['now_tz'].replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None) + timedelta(days=1), is_dst=None).astimezone(self.tz)
		self.templateDict['tomorrowend_tz'] = self.tz.localize(self.templateDict['now_tz'].replace(hour=23, minute=59, second=59, microsecond=999999, tzinfo=None) + timedelta(days=1), is_dst=None).astimezone(self.tz)	
		
		self.templateDict['monthstart_tz'] = datetime(self.templateDict['now_tz'].year, self.templateDict['now_tz'].month, 1)
		self.templateDict['monthend_tz'] = datetime(self.templateDict['now_tz'].year, self.templateDict['now_tz'].month + 1, 1) - timedelta(days=1)
		self.templateDict['lastmonthend_tz'] = self.templateDict['monthstart_tz'] - timedelta(days=1)
		self.templateDict['lastmonthstart_tz'] = datetime(self.templateDict['lastmonthend_tz'].year, self.templateDict['lastmonthend_tz'].month, 1)
		
		self.templateDict['yearstart_tz'] = self.tz.localize(datetime(self.templateDict['now_tz'].year, 1, 1).replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None), is_dst=None).astimezone(self.tz)
		self.templateDict['yearend_tz'] = self.tz.localize(datetime(self.templateDict['now_tz'].year, 12, 31).replace(hour=23, minute=59, second=59, microsecond=999999, tzinfo=None), is_dst=None).astimezone(self.tz)
		self.templateDict['lastyearstart_tz'] = self.tz.localize(datetime(self.templateDict['now_tz'].year-1, 1, 1).replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None), is_dst=None).astimezone(self.tz)
		self.templateDict['lastyearend_tz'] = self.tz.localize(datetime(self.templateDict['now_tz'].year-1, 12, 31).replace(hour=23, minute=59, second=59, microsecond=999999, tzinfo=None), is_dst=None).astimezone(self.tz)
		

		self.templateDict['now_notz'] = datetime.now()
		self.templateDict['todaystart_notz'] = self.templateDict['now_notz'].replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
		self.templateDict['todayend_notz'] = self.templateDict['now_notz'].replace(hour=23, minute=59, second=59, microsecond=999999, tzinfo=None)
		self.templateDict['yesterdaystart_notz'] = self.templateDict['now_notz'].replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None) - timedelta(days=1)
		self.templateDict['yesterdayend_notz'] = self.templateDict['now_notz'].replace(hour=23, minute=59, second=59, microsecond=999999, tzinfo=None) - timedelta(days=1)
		self.templateDict['tomorrowstart_notz'] = self.templateDict['now_notz'].replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None) + timedelta(days=1)
		self.templateDict['tomorrowend_notz'] = self.templateDict['now_notz'].replace(hour=23, minute=59, second=59, microsecond=999999, tzinfo=None) + timedelta(days=1)
		
		self.templateDict['monthstart_notz'] = datetime(self.templateDict['now_notz'].year, self.templateDict['now_notz'].month, 1)
		self.templateDict['monthend_notz'] = datetime(self.templateDict['now_notz'].year, self.templateDict['now_notz'].month + 1, 1) - timedelta(days=1)
		self.templateDict['lastmonthend_notz'] = self.templateDict['monthstart_notz'] - timedelta(days=1)
		self.templateDict['lastmonthstart_notz'] = datetime(self.templateDict['lastmonthend_notz'].year, self.templateDict['lastmonthend_notz'].month, 1)
		
		self.templateDict['yearstart_notz'] = datetime(self.templateDict['now_notz'].year, 1, 1).replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
		self.templateDict['yearend_notz'] = datetime(self.templateDict['now_notz'].year, 12, 31).replace(hour=23, minute=59, second=59, microsecond=999999, tzinfo=None)
		self.templateDict['lastyearstart_notz'] = datetime(self.templateDict['now_notz'].year-1, 1, 1).replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
		self.templateDict['lastyearend_notz'] = datetime(self.templateDict['now_notz'].year-1, 12, 31).replace(hour=23, minute=59, second=59, microsecond=999999, tzinfo=None)
		
	def replacePlaceHolders(self):
		for key, value in TemplateKeysDict().items():
			self.QueryString = self.QueryString.replace(key, "'"+str(self.templateDict[value])+"'")
		self.QueryString = self.QueryString.replace("\r\n", " ")
		self.QueryString = self.QueryString.replace("\n", " ")