import csv
import json
from django.core.management.base import BaseCommand
from gameLogics.models import Location  # Replace with your model

class Command(BaseCommand):
    help = 'Import data from a CSV file into a model'

    def handle(self, *args, **options):
        csv_file_path = "/Users/macbookpro/DjangoProjects/SpaceGame/SpaceGame/gameLogics/csv/locations.csv"

        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                name = row[1]
                gains_tax_rate = int(row[2])
                docking_fee = row[3]
                weekly_interest = row[4]
                marketplace = row[5]
                repair_bay = row[6]
                med_bay = row[7]
                pasengers_crew = row[8]
                missions_reqs = row[9]
                lender = row[10]
                storage = row[11]
                ship_dealer = row[12]
                leisure = row[13]

                # Create a new instance of YourModel or update an existing one
                model_instance = Location.objects.filter(name=name).first()
                if not model_instance:
                    model_instance = Location()
                    model_instance.name = name
                    model_instance.gains_tax_rate = gains_tax_rate
                    model_instance.docking_fee = docking_fee
                    model_instance.weekly_interest = weekly_interest
                    model_instance.marketplace = marketplace
                    model_instance.repair_bay = repair_bay
                    model_instance.med_bay = med_bay
                    model_instance.pasengers_crew = pasengers_crew
                    model_instance.missions_reqs = missions_reqs
                    model_instance.lender = lender
                    model_instance.storage = storage
                    model_instance.ship_dealer = ship_dealer
                    model_instance.leisure = leisure
                    model_instance.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
