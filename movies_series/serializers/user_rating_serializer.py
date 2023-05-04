from rest_framework import serializers
from movies_series.domain import UserRating

class UserRatingSerializer(serializers.ModelSerializer):
    user = serializers.UUIDField(
      write_only=True,
      required=False,
      allow_null=True
    )
    movie_series = serializers.UUIDField(
      write_only=True,
      required=False,
      allow_null=True
    )
    class Meta:
        model = UserRating
        fields = '__all__'