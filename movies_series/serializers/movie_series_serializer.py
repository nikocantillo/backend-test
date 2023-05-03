from rest_framework import serializers
from movies_series.domain import MovieSeries
from movies_series.serializers import GenderSerializer, TypeSerializer


class MovieSeriesSerializer(serializers.ModelSerializer):
    gender = GenderSerializer(many=True)
    type = TypeSerializer()

    class Meta:
        model = MovieSeries
        fields = '__all__'
