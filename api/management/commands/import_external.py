import csv
import os

from datetime import datetime
from dateutil.parser import isoparse
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from api.models import Ship, Position

class Command(BaseCommand):
    help = 'Import Position from external csv File Located in "data"'

    def add_arguments(self, parser):
        parser.add_argument('file_name', help='name of the file to import')

    def handle(self, *args, **options):
        file_name = options['file_name']
        dir_fd = os.path.join(settings.BASE_DIR, 'data')

        file_path = os.path.join(dir_fd, file_name)
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                imo = int(row[0])
                date = isoparse(row[1])
                lat = row[2]
                lon = row[3]
                try:
                    ship = Ship.get_by_imo(imo)
                except Ship.DoesNotExist:
                    self.stdout.write(self.style.ERROR('No Ship found in the database with the IMO "%s"' % imo))
                    # raise CommandError('No Ship found in the database with the IMO "%s"' % imo)
                    continue
                Position(timestamp=date,
                    ship=ship,
                    latitude=lat,
                    longitude=lon).save()
                # break
                # input("Press Enter to continue...")
        self.stdout.write(self.style.SUCCESS('Successfully import the file "%s"' % file_name))