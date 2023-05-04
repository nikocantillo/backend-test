from django.shortcuts import get_object_or_404
from rest_framework import generics, status, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from movies_series.domain import MovieSeries, UserRating, Gender, Type
from movies_series.serializers import MovieSeriesSerializer, UserRatingSerializer
import random


class MarkMovieSeriesAsWatchedView(viewsets.ModelViewSet):
    queryset = UserRating.objects.all()
    serializer_class = UserRatingSerializer
    permission_classes = [IsAuthenticated]
    
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        instance.watched = True
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()
    

class RateMovieSeriesView(viewsets.ModelViewSet):
    queryset = UserRating.objects.all()
    serializer_class = UserRatingSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user_rating = self.get_object()
        rating = request.data.get('rating', None)
        if rating is not None and 1 <= rating <= 5:
            user_rating.rating = rating
            user_rating.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(
                {"detail": "Invalid rating value, it should be between 1 and 5."},
                status=status.HTTP_400_BAD_REQUEST
            )