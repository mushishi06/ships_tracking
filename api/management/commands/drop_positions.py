import csv
import os

from datetime import datetime
from dateutil.parser import isoparse
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from api.models import Ship, Position

class Command(BaseCommand):
    help = 'Delete all Position for an IMO'

    def add_arguments(self, parser):
        parser.add_argument('imo', help='IMO nuber')

    def handle(self, *args, **options):
        imo = options['imo']
        try:
            ship = Ship.get_by_imo(imo)
        except Ship.DoesNotExist:
            self.stdout.write(self.style.ERROR('No Ship found in the database with the IMO "%s"' % imo))
            raise CommandError('No Ship found in the database with the IMO "%s"' % imo)
        Position.objects.filter(ship=ship).all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully delete all Position for IMO "%s"' % imo))