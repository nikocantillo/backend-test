from django.core.management.base import BaseCommand
from authentication.domain.user import User
from movies_series.domain.movies_series_model import MovieSeries
from movies_series.domain.user_rating_model import UserRating


class Command(BaseCommand):
    help = 'Inserts sample user rating data'

    def handle(self, *args, **options):
        user1 = User.objects.get(username='nikolas1')
        user2 = User.objects.get(username='nikolas2')
        movie1 = MovieSeries.objects.get(name='The Godfather')
        movie2 = MovieSeries.objects.get(name='Breaking Bad')

        UserRating.objects.create(user=user1, movie_series=movie1, rating=8)
        UserRating.objects.create(user=user2, movie_series=movie2, rating=9)

        self.stdout.write(self.style.SUCCESS('Sample data inserted successfully.'))