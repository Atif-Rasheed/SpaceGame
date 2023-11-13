import csv
import json
from django.core.management.base import BaseCommand
from gameLogics.models import Distance  # Replace with your model

class Command(BaseCommand):
    help = 'Import data from a CSV file into a model'

    def handle(self, *args, **options):
        csv_file_path = "/Users/macbookpro/DjangoProjects/SpaceGame/SpaceGame/gameLogics/csv/Distance.csv"

        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                location1 = row[0]
                location2 = row[1]
                distance = row[2]
                
                # Create a new instance of YourModel or update an existing one
                # model_instance = Distance.objects.filter(location1=location1,location2=location2).first()
                # if not model_instance:
                model_instance = Distance()
                model_instance.location1 = location1
                model_instance.location2 = location2
                model_instance.distance = distance
                model_instance.save()
                # Print the instance data
                print(f"Instance created: {model_instance}")
 
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
