from rest_framework import serializers
from movies_series.domain import Movie, UsersRating

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'genre', 'type', 'viewed_by', 'average_rating']

class UserRatingSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UsersRating
        fields = ['movie', 'user', 'rating']