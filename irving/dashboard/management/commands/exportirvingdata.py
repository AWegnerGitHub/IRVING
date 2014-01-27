from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.core import serializers
from django.db.models.loading import get_model
from dashboard import models
import re, os, sys

class Command(BaseCommand):
	args = 'system_model [system_id]'
	help = 'Exports data and prepares for import in another system'

	def handle(self, *args, **options):
		if len(args) > 1:
			self.dump_system_data(args[0], system_id = args[1])
		else:
			if args[0] == 'Permissions':
				self.dump_permissions()
			else:
				self.dump_system_data(args[0])

			
	def dump_system_data(self, model = None, system_id = None):
		if model:
			modelN = get_model(model.split(".")[0],model.split(".")[1])
			if modelN == models.QueryData:
				if not system_id:
					data = serializers.serialize("json", modelN.objects.all())
					data = self.cleanExport(data)
					system_id = None
				else:
					data = serializers.serialize("json", modelN.objects.filter(system=system_id))
					data = self.cleanExport(data)
			else:
				data = serializers.serialize("json", modelN.objects.all())
				data = self.cleanExport(data)
				system_id = None
			self.writeExport(model, system_id, data)
			
	def dump_permissions(self):
		sys.stdout = open(os.path.join(os.getcwd(), "dashboard/IMPORT_FILES/system_permissions.json"), "w")
		call_command('dumpdata', 'auth.group', 'contenttypes.contenttype', 'auth.permission', format="json", indent=4)
		sys.stdout.close()

	def cleanExport(self, dString):
		dString = re.sub('"pk": [0-9]{1,5}', '"pk": null', dString)
		dString = re.sub('"system": [0-9]{1,5}', '"system": null', dString)
		dString = re.sub('""', 'null', dString)
		return dString

	def writeExport(self, modelName, filterSystem, dString):
		if filterSystem:
			systemName = models.System.objects.filter(id=filterSystem)[0].database_name
		else:
			systemName = 'all'
		if os.path.isdir(os.path.join(os.getcwd(), "dashboard/IMPORT_FILES/")):
			out = open(os.path.join(os.getcwd(), "dashboard/IMPORT_FILES/", modelName + "_system_" + systemName + ".json"), "w")
			out.write(dString)
			out.close()
		else:
			raise IOError(os.path.join(os.getcwd(), "dashboard/IMPORT_FILES/ does not exist"))