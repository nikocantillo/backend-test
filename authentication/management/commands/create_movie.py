from django.core.management.base import BaseCommand
from movies_series.domain import MovieSeries, Gender, Type, Movie
from django.utils.crypto import get_random_string

# class Command(BaseCommand):
#     help = 'Create random movies'

#     def add_arguments(self, parser):
#         parser.add_argument('total', type=int, help='Indicates the number of movies to be created')

#     def handle(self, *args, **kwargs):
#         total = kwargs['total']
#         types = Type.objects.all()
#         gender = Gender.objects.all()

#         for _ in range(total):
#             Movie.objects.create(
#                 name=get_random_string(10),
#                 type=types.order_by('?').first(),
#                 number_of_views=0,
#                 total_score=0,
#                 number_of_ratings=0
#             ).gender.set(gender.order_by('?')[:2])

#         self.stdout.write(self.style.SUCCESS(f'Successfully created {total} movies'))


class Command(BaseCommand):
    help = 'Inserta películas en la base de datos'

    def add_arguments(self, parser):
        parser.add_argument('movies', type=str, nargs='+', help='Lista de películas para insertar')
        parser.add_argument('--type', type=str, required=True, help='Tipo de las películas (Serie o Película)')

    def handle(self, *args, **options):
        movie_type_name = options['type']
        movie_type, _ = Type.objects.get_or_create(name=movie_type_name)

        for movie_name in options['movies']:
            movie = Movie(name=movie_name, genre="Drama", type=movie_type)
            movie.save()
            self.stdout.write(self.style.SUCCESS(f'Película "{movie_name}" insertada con éxito'))