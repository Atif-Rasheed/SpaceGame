import csv
import json
from django.core.management.base import BaseCommand
from gameLogics.models import Ships,Route  # Replace with your model

class Command(BaseCommand):
    help = 'Import data from a CSV file into a model'

    def handle(self, *args, **options):
        csv_file_path = "/Users/macbookpro/DjangoProjects/SpaceGame/SpaceGame/gameLogics/csv/Ships.csv"

        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                name = row[0]
                size = row[1]
                type = row[2]
                value = row[3]
                crew = row[4]
                cargo = row[5]
                fuel = row[6]
                passengers = row[7]
                upgrade_slot = row[8]
                upgrade1 = row[9]
                upgrade2 = row[10]
                upgrade3 = row[11]
                upgrade4 = row[12]
                upgrade5 = row[13]
                rid = row[14]
                # Create a new instance of YourModel or update an existing one
                model_instance = Ships.objects.filter(name=name,rid=rid).first()
                if not model_instance:
                    model_instance = Ships()
                    model_instance.name = name
                    model_instance.size = size
                    model_instance.type = type
                    model_instance.value = value
                    model_instance.crew = crew
                    model_instance.cargo = cargo
                    model_instance.fuel = fuel
                    model_instance.passengers = passengers
                    model_instance.upgrade_slot = upgrade_slot
                    model_instance.rid = Route.objects.filter(rid=rid).first()
                    model_instance.upgrade1 = upgrade1
                    model_instance.upgrade2 = upgrade2
                    model_instance.upgrade3 = upgrade3
                    model_instance.upgrade4 = upgrade4
                    model_instance.upgrade5 = upgrade5
                    model_instance.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
