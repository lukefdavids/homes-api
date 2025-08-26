from homesapi.models import HomeType
from rest_framework import serializers

class HomeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeType
        fields = ['id', 'name']