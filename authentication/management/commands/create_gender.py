from django.core.management.base import BaseCommand
from movies_series.domain import Gender
from datetime import datetime
from django.contrib.auth.models import UserManager

class Command(BaseCommand):
    help = 'help text'

    def handle(self, *args, **options):
        gender = Gender(
            name = 'Acción',
            code = 'accion'
        )
        gender.save()
        gender1 = Gender(
            name = 'Anime',
            code = 'anime'
        )
        gender1.save()
        gender2 = Gender(
            name = 'Dramas',
            code = 'dramas'
        )
        gender2.save()
        gender3 = Gender(
            name = 'Fantasía',
            code = 'fantasia'
        )
        gender3.save()
        terror = Gender(
            name = 'Terror',
            code = 'terror'
        )
        terror.save()