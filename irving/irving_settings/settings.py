# Django settings for IRVING project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Name', 'Email'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'irving.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
	'db1': {
		'ENGINE': 'django.db.backends.oracle',
		'NAME': '',
		'OPTIONS': {'threaded': True,},
		'USER': "",
		'PASSWORD': "",
		'HOST': '',
		'PORT': "1521",
	},
	'db2': {
		'ENGINE': 'django.db.backends.oracle',
		'NAME': '',
		'OPTIONS': {'threaded': True,},
		'USER': "", 
		'PASSWORD': "",
		'HOST': '',
		'PORT': "1521",
	},
	'db3': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'OPTIONS': {},
        'USER': "",
        'PASSWORD': "",
        'HOST': '',
        'PORT': "3306",
    },
	'db4': {
        'ENGINE': 'sqlserver_ado',
        'NAME': '',
        'OPTIONS': {},
        'USER': "",
        'PASSWORD': "",
        'HOST': '',
    },	
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = "irving_settings/sitestatic"

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
	'dashboard.LoginRequiredMiddleware.LoginRequiredMiddleware',
)

ROOT_URLCONF = 'irving_settings.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'irving_settings.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	'irving_settings/templates',
	'irving_settings/templates/dashboard'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
	'django.contrib.humanize',
	'smart_selects',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'dashboard',
	'login',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTH_PROFILE_MODULE = "dashboard.UserProfile"

DATABASE_ROUTERS = ['dashboard.DatabaseRouter.DBRouter',]

# A routing map to show which applications should route to which databases
# Not used with the DBRouter DATABASE_ROUTER, instead it is used with the 
# DatabaseAppsRouter class
#DATABASE_APPS_MAPPING = {'dashboard' : 'tm'}

LOGIN_URL = '/login/'

LOGIN_EXEMPT_URLS = (
# r'^about\.html$',
# r'^legal/', # allow any URL under /legal/*
  r'^adminarea/',
  r'^static/',
)

# Session information
SESSION_SAVE_EVERY_REQUEST = True
	# Time for a session to be valid (in seconds)
	# Default is 2 hours = 7200 seconds
SESSION_EXPIRE_TIME = 7200