from django.core.management.base import BaseCommand
from movies_series.domain import Type
from datetime import datetime
from django.contrib.auth.models import UserManager

class Command(BaseCommand):
    help = 'help text'

    def handle(self, *args, **options):
        type = Type(
            name = 'Serie',
            code = 'serie'
        )
        type.save()
        type1 = Type(
            name = 'Movie',
            code = 'movie'
        )
        type1.save()