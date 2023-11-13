import csv
import json
from django.core.management.base import BaseCommand
from gameLogics.models import Crews  # Replace with your model

class Command(BaseCommand):
    help = 'Import data from a CSV file into a model'

    def handle(self, *args, **options):
        csv_file_path = "/Users/macbookpro/DjangoProjects/SpaceGame/SpaceGame/gameLogics/csv/Crew.csv"

        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                name = row[0]
                profession = row[1]
                weeklySalary = row[2]
                fromw = row[3]
                health = row[4]
                stress = row[5]
                resolve = row[6]
                hunger = row[7]
                condition1 = row[8]
                condition2 = row[9]
                condition3 = row[10]
          
                # Create a new instance of YourModel or update an existing one
                model_instance = Crews.objects.filter(name=name).first()
                if not model_instance:
                    model_instance = Crews()
                    model_instance.name = name
                    model_instance.profession = profession
                    model_instance.weeklySalary = weeklySalary
                    model_instance.fromW = fromw
                    model_instance.health = health
                    model_instance.stress = stress
                    model_instance.resolve = resolve
                    model_instance.hunger = hunger
                    model_instance.condition1 = condition1
                    model_instance.condition2 = condition2
                    model_instance.condition3 = condition3
                    model_instance.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
