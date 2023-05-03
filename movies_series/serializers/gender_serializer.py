from rest_framework import serializers
from movies_series.domain import Gender

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'