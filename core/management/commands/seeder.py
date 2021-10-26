import faker as faker
from django.core.management.base import BaseCommand
from django_seed import Seed
from core.models import Position, Employee, Salary


class Command(BaseCommand):
    help = 'seeder'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        fakes = faker.Faker()
        level = (a for a in Position.LEVEL_CHOICES)
        seeder.add_entity(Position, 5, {
            'position': lambda x: fakes.job(),
            'level': lambda x: next(level),
        })

        seeder.add_entity(Employee, 10, {
            'first_name': lambda x: fakes.first_name_male(),
            'last_name': lambda x: fakes.last_name_male(),
            'patronymic': lambda x: fakes.first_name_male(),
            'position': lambda x: Position.objects.order_by('?')[0],
            'employment_date': lambda x: fakes.date(),
            'chief': lambda x: Employee.objects.last(),
            'wages': lambda x: fakes.pydecimal(positive=True, right_digits=2, max_value=15000),
        })

        seeder.add_entity(Salary, 10, {
            'employee': lambda x: Employee.objects.order_by("?")[0],
            'date_paid': lambda x: fakes.date(),
            'sum_paid': lambda x: fakes.pydecimal(positive=True, right_digits=2, max_value=15000),
        })

        seeder.execute()
        
