from rest_framework import generics, mixins, filters, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from movies_series.domain import Movie, UsersRating
from movies_series.serializers import MovieSerializer, UserRatingSerializer
from django.db.models import Avg
import random


class MovieMarkAsWatchedViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        movie = self.get_object()
        user = request.user
        if user in movie.viewed_by.all():
            return Response(
                {"detail": "Ya has visto esta película o serie."},
                status=status.HTTP_400_BAD_REQUEST)
        movie.viewed_by.add(user)
        movie.save()
        serializer = self.serializer_class(movie)
        return Response(serializer.data)

class MovieRateViewSet(viewsets.ModelViewSet):
    queryset = UsersRating.objects.all()
    serializer_class = UserRatingSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        movie_id = request.data.get('movie_id', None)
        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response(
                {"detail": "La película o serie no existe."}, 
                status=status.HTTP_404_NOT_FOUND
            )

        if UsersRating.objects.filter(movie=movie, user=user).exists():
            return Response(
                {"detail": "Ya has puntuado esta película o serie."}, 
                status=status.HTTP_400_BAD_REQUEST)

        rating = request.data.get('rating', None)
        if rating is None or not (1 <= int(rating) <= 5):
            return Response(
                {"detail": "La puntuación debe estar entre 1 y 5."}, 
                status=status.HTTP_400_BAD_REQUEST)

        user_rating = UsersRating(movie=movie, user=user, rating=rating)
        user_rating.save()

        avg_rating = UsersRating.objects\
            .filter(movie=movie).aggregate(Avg('rating'))['rating__avg']
        movie.average_rating = avg_rating
        movie.save()

        serializer = self.serializer_class(user_rating)
        return Response(serializer.data)