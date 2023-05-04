from django.core.management.base import BaseCommand
from movies_series.domain import MovieSeries, Gender, Type
from django.utils.crypto import get_random_string


# class Command(BaseCommand):
#     help = 'Insert multiple movies and series'

#     def handle(self, *args, **kwargs):
#         movies_series = [
#             {
#                 'name': 'Pelicula 1',
#                 'gender': ['097c1b133389427884462ccfe5940c61'],
#                 'type': 'movie',
#                 'number_of_views': 100,
#                 'total_score': 80,
#                 'number_of_ratings': 10
#             },
#             {
#                 'name': 'Serie 1',
#                 'gender': ['097c1b133389427884462ccfe5940c61'],
#                 'type': 'serie',
#                 'number_of_views': 50,
#                 'total_score': 70,
#                 'number_of_ratings': 5
#             },
#             {
#                 'name': 'Pelicula 2',
#                 'gender': ['097c1b133389427884462ccfe5940c61'], 
#                 'type': 'movie',
#                 'number_of_views': 0,
#                 'total_score': 0,
#                 'number_of_ratings': 0
#             },
#             {
#                 'name': 'Serie 2',
#                 'gender': ['097c1b133389427884462ccfe5940c61'], 
#                 'type': 'serie',
#                 'number_of_views': 0,
#                 'total_score': 0,
#                 'number_of_ratings': 0
#             },
#             {
#                 'name': 'Pelicula 3',
#                 'gender': ['fa9806fe306845bea9189e91e7f4feaf'],  
#                 'type': 'movie',
#                 'number_of_views': 0,
#                 'total_score': 0,
#                 'number_of_ratings': 0
#             },
#             {
#                 'name': 'Serie 3',
#                 'gender': ['5a8f144e89e04f84b3d5979698fb9f7b'],  
#                 'type': 'serie',
#                 'number_of_views': 0,
#                 'total_score': 0,
#                 'number_of_ratings': 0
#             },
#         ]

#         for movie_serie in movies_series:
#             type_obj, _ = Type.objects.get_or_create(id=movie_serie['type'])
#             movie_serie_obj = MovieSeries(
#                 name=movie_serie['name'],
#                 type=type_obj,
#                 number_of_views=movie_serie['number_of_views'],
#                 total_score=movie_serie['total_score'],
#                 number_of_ratings=movie_serie['number_of_ratings']
#             )
#             movie_serie_obj.save()
#             for gender_id in movie_serie['gender']:
#                 genre_obj, _ = Gender.objects.get_or_create(id=gender_id)
#                 movie_serie_obj.gender.add(genre_obj)

#             self.stdout.write(self.style.SUCCESS(f"Movie/Serie '{movie_serie_obj.name}' created."))


class Command(BaseCommand):
    help = 'Create random movies'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of movies to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        types = Type.objects.all()
        gender = Gender.objects.all()

        for _ in range(total):
            MovieSeries.objects.create(
                name=get_random_string(10),
                type=types.order_by('?').first(),
                number_of_views=0,
                total_score=0,
                number_of_ratings=0
            ).gender.set(gender.order_by('?')[:2])

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} movies'))