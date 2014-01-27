from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.db.models.loading import get_model
from dashboard import models
import re, os, sys

class Command(BaseCommand):
	args = 'file <system_id>'
	help = 'Imports data and relates it to a specific system'

	def handle(self, *args, **options):
		error = False
		if args[0] != "system_permissions.json":
			app = args[0].split('.')[0]
			model = args[0].split('.')[1].split('_')[0]
			file = args[0]
			modelN = get_model(app,model)
			if modelN == models.QueryData:
				try:
					self.clean_model(file, system_id=args[1] )
				except IndexError:
					print """A system to associate all of the queries in %s must be assigned by passing the system id as a parameter 
					importirvingdata %s <system_id>
					Nothing has been imported""" % (file, file)
					error = True
		else:
			file = args[0]
					
		if not error:
			call_command('loaddata', os.path.join(os.getcwd(), "dashboard/IMPORT_FILES/",file))

		
	def clean_model(self, modelName, system_id = None):

		if os.path.isdir(os.path.join(os.getcwd(), "dashboard/IMPORT_FILES/")):
			iFile = open(os.path.join(os.getcwd(), "dashboard/IMPORT_FILES/", modelName), "r")
			d = iFile.read()
			iFile.close()
			d = re.sub('"system": null', '"system": ' + str(system_id), d)

			iFile = open(os.path.join(os.getcwd(),"dashboard/IMPORT_FILES/", modelName), "w")
			iFile.write(d)
			iFile.close()



