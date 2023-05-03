from django.shortcuts import get_object_or_404
from rest_framework import generics, status, mixins
from rest_framework.response import Response
from movies_series.domain import MovieSeries, UserRating, Gender, Type
from movies_series.serializers import MovieSeriesSerializer, UserRatingSerializer
import random


class MarkMovieSeriesAsWatchedView(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = UserRating.objects.all()
    serializer_class = UserRatingSerializer
    lookup_url_kwarg = 'user_rating_id'

    def patch(self, request, *args, **kwargs):
        user_rating = self.get_object()
        user_rating.watched = True
        user_rating.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class RateMovieSeriesView(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = UserRating.objects.all()
    serializer_class = UserRatingSerializer
    lookup_url_kwarg = 'user_rating_id'

    def patch(self, request, *args, **kwargs):
        user_rating = self.get_object()
        rating = request.data.get('rating', None)
        if rating is not None and 1 <= rating <= 5:
            user_rating.rating = rating
            user_rating.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"detail": "Invalid rating value, it should be between 1 and 5."},
                status=status.HTTP_400_BAD_REQUEST
            )