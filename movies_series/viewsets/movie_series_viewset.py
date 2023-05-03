from django.shortcuts import get_object_or_404
from rest_framework import generics, status, mixins
from rest_framework.response import Response
from movies_series.domain import MovieSeries, UserRating, Gender, Type
from movies_series.serializers import MovieSeriesSerializer, UserRatingSerializer
import random



class RandomMovieSeriesView(generics.GenericAPIView):
    queryset = MovieSeries.objects.all()
    serializer_class = MovieSeriesSerializer

    def get(self, request, *args, **kwargs):
        movie_series = random.choice(self.queryset)
        serializer = self.serializer_class(movie_series)
        return Response(serializer.data)
    


class MovieSeriesListView(generics.ListAPIView):
    queryset = MovieSeries.objects.all()
    serializer_class = MovieSeriesSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.apply_filters(queryset)
        queryset = self.apply_ordering(queryset)
        return queryset

    def apply_filters(self, queryset):
        name = self.request.query_params.get('name', None)
        movie_type = self.request.query_params.get('type', None)
        genre = self.request.query_params.get('genre', None)

        if name:
            queryset = queryset.filter(name__icontains=name)
        if movie_type:
            queryset = queryset.filter(type__name=movie_type)
        if genre:
            queryset = queryset.filter(genre__name=genre)

        return queryset

    def apply_ordering(self, queryset):
        order_by = self.request.query_params.get('order_by', None)
        if order_by and order_by in ['name', 'type', 'gender', 'average_score']:
            if order_by == 'type':
                order_by = 'type__name'
            elif order_by == 'gender':
                order_by = 'gender__name'
            queryset = queryset.order_by(order_by)

        return queryset