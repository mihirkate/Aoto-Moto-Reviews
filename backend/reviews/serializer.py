from rest_framework import serializers
from .models import Car
 
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
    def validate_name(self, value):
        if Car.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("Car already exists")
        return value