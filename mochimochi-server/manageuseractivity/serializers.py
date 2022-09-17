from rest_framework import serializers
from .models import EnrollInformation

class EnrollInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrollInformation
        fields=['user','date']

