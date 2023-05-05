from django.shortcuts import get_object_or_404
from rest_framework import generics, status, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from movies_series.domain import Movie, Type
from movies_series.serializers import MovieSerializer, UserRatingSerializer
import random
from django.db.models import Q
from rest_framework.decorators import action

class RandomMovieSeriesViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def random_movie(self, request, *args, **kwargs):
        movie = random.choice(self.queryset)
        serializer = self.serializer_class(movie)
        return Response(serializer.data)
    
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.apply_filters(queryset)
        queryset = self.apply_ordering(queryset)
        return queryset

    def apply_filters(self, queryset):
        search = self.request.GET.get('search', None)
        name = self.request.query_params.get('name', None)
        movie_type = self.request.query_params.get('type', None)
        genre = self.request.query_params.get('genre', None)
        filters = Q()
        if search:
            search_filters = (
                Q(name__icontains=search)
                | Q(type__name__icontains=search)
                | Q(genre__icontains=search)
            )
            filters &= search_filters
        if name:
            queryset = queryset.filter(name__icontains=name)
        if movie_type:
            queryset = queryset.filter(type__name=movie_type)
        if genre:
            queryset = queryset.filter(genre__icontains=genre)
        queryset = queryset.filter(filters)
        return queryset
    

    def apply_ordering(self, queryset):
        order_by = self.request.query_params.get('order_by', None)
        if order_by and order_by in ['name', 'type', 'genre']:
            if order_by == 'type':
                order_by = 'type__name'
            elif order_by == 'genre':
                order_by = 'genre'
            queryset = queryset.order_by(order_by)

        return queryset
    
    @action(detail=False, methods=['get'])
    def list_filtered(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = self.apply_filters(queryset)
        queryset = self.apply_ordering(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = MovieSerializer(page, many=True).data
            return self.get_paginated_response(serializer)

        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)