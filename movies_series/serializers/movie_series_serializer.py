from rest_framework import serializers
from movies_series.domain import MovieSeries
from movies_series.serializers.gender_serializer import GenderSerializer
from movies_series.serializers.type_serializer import TypeSerializer


class MovieSeriesSerializer(serializers.ModelSerializer):
    gender = GenderSerializer(many=True)
    type = TypeSerializer()

    class Meta:
        model = MovieSeries
        fields = '__all__'
