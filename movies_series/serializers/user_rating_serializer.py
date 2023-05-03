from rest_framework import serializers
from movies_series.domain import UserRating

class UserRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRating
        fields = '__all__'