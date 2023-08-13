from django.core.management.base import BaseCommand
from django.core.management import call_command
from app.models import CoursesOfCategory

class Command(BaseCommand):
    help = 'Dump data excluding a specific object'

    def handle(self, *args, **options):
        queryset = CoursesOfCategory.objects.exclude(id=25)  # Exclude the object with ID 123
        call_command('dumpdata', 'myapp.MyModel', stdout=self.stdout, queryset=queryset)
