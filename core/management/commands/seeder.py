import faker as faker
from django.core.management.base import BaseCommand
from django_seed import Seed
from core.models import *


class Command(BaseCommand):
    help = 'seeder'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        fakes = faker.Faker()

        
