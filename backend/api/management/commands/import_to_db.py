import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Import ingredients to DB from json'

    def add_arguments(self, parser):
        parser.add_argument('ingredients',
                            default='ingredients.json',
                            nargs='?',
                            type=str)

    def handle(self, *args, **options):
        try:
            with open(os.path.join(settings.MEDIA_ROOT + '/data/',
                                   options['ingredients']),
                      'r',
                      encoding='utf-8') as f:
                data = json.load(f)
                for ingredient in data:
                    try:
                        Ingredient.objects.create(
                            name=ingredient['name'],
                            measurement_unit=ingredient['measurement_unit'])
                    except IntegrityError:
                        print(f'The database already has: {ingredient["name"]}'
                              f'({ingredient["measurement_unit"]})')

        except FileNotFoundError:
            raise CommandError('File is not in the directory media/data')
