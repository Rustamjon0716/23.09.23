from rest_framework import serializers
from .models import LaptopModel

class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptopModel
        fields = ('__all__')