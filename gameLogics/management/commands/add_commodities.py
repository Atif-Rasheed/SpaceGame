import csv
import json
from django.core.management.base import BaseCommand
from gameLogics.models import Commodities  # Replace with your model

class Command(BaseCommand):
    help = 'Import data from a CSV file into a model'

    def handle(self, *args, **options):
        csv_file_path = "/home/RajaAtif1225/SpaceGame/gameLogics/csv/Commodities.csv"

        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                name = row[0]
                minimum_price = row[1]
                maximum_price = row[2]
                fragile = row[3]
                perishable = row[4]
                edible = row[5]
                earth = row[6]
                earth_moon = row[7]
                mars = row[8]
                phobos = row[9]
                deimos = row[10]
                europa = row[11]
                titan = row[12]
                ganymede = row[13]
                enceladus = row[14]
                io = row[15]
                callisto = row[16]
                triton = row[17]

                
                # Create a new instance of YourModel or update an existing one
                model_instance = Commodities.objects.filter(name=name,min_price=minimum_price,max_price=maximum_price).first()
                if not model_instance:
                    model_instance = Commodities()
                    model_instance.name = name
                    model_instance.min_price = minimum_price
                    model_instance.max_price = maximum_price
                    model_instance.fragile = fragile
                    model_instance.perishable = perishable
                    model_instance.edible = edible
                    model_instance.earth = earth
                    model_instance.moon = earth_moon
                    model_instance.mars = mars
                    model_instance.phobos = phobos
                    model_instance.europa = europa
                    model_instance.titan = titan
                    model_instance.ganymede = ganymede
                    model_instance.enceladus = enceladus
                    model_instance.io = io
                    model_instance.callisto = callisto
                    model_instance.triton = triton
                    model_instance.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
