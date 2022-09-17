from rest_framework import serializers

from .models import User, UserManager


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'username', 'email')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return UserManager().create_user(
            password=validated_data['password'],
            username=validated_data['username'],
            email=validated_data['email'],
        )
