from rest_framework import serializers
from movies_series.domain import Movie, UsersRating

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'genre', 'type', 'viewed_by', 'average_rating']

    def to_representation(self, data):
        data_return = {
            'id': data.id if data.id else None,
            'name': data.name if data.name else None,
            'genre': data.genre if data.genre else None,
            'type': data.type.name if data.type else None,
            'viewed_by': [user.username for user in data.viewed_by.all()],
            'average_rating': data.average_rating if data.average_rating else None
        }
        return data_return

class UserRatingSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UsersRating
        fields = ['movie', 'user', 'rating']