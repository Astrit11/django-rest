from .models import Breed, Dog
from rest_framework import serializers

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('name', 'image', 'breed')
