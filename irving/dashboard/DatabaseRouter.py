from django.conf import settings

# Replaces DatabaseAppsRouter.py by allowing each model the be set
# to connect to a specific database.

from django.db import connections

class DBRouter(object):
    """
	A router to control model access to specific database
	"""

    def db_for_read(self, model, **hints):
        if hasattr(model,'connection_name'):
            return model.connection_name
        return None

    def db_for_write(self, model, **hints):
        if hasattr(model,'connection_name'):
            return model.connection_name
        return None

	def allow_syncdb(self, db, model):
		print model.connection_name
		if hasattr(model, 'allow_sync'):
			if not model.allow_sync:
				return False
			if hasattr(model,'connection_name'):
				return model.connection_name == db
			return db == 'default'
		else:
			return False


		