from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Prints the PATH environment variable'

    def handle(self, *args, **kwargs):
        path = os.environ.get('PATH')
        self.stdout.write(self.style.SUCCESS(f'PATH: {path}'))
