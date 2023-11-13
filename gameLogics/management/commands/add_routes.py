import csv
import json
from django.core.management.base import BaseCommand
from gameLogics.models import Route  # Replace with your model

class Command(BaseCommand):
    help = 'Import data from a CSV file into a model'

    def handle(self, *args, **options):
        csv_file_path = "/Users/macbookpro/DjangoProjects/SpaceGame/SpaceGame/gameLogics/csv/routes.csv"

        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                rid = int(row[0])
                values = row[1:]
                values = [value.strip() for value in values]
                # Convert the values list to a JSON string
                values_json = json.dumps(values)
                # Create a new instance of YourModel or update an existing one
                model_instance, created = Route.objects.get_or_create(rid=rid)
                if not created:
                    model_instance.rid = rid
                model_instance.route_details = values_json
                model_instance.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
