from userauthentication.models import User
from rest_framework import serializers
from .models import Rooms, UsersRooms
from userauthentication.serializers import UserSerializer

class roomSerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all()
    )
    class Meta:
        model = Rooms
        fields = ("id", "date", "zoom_url", "user")
    
    def get_user(self, obj):
        return obj.user.all().values_list('id', flat=True)

class userRoomSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()
    room_id = serializers.SerializerMethodField()
    participate=serializers.BooleanField()
    class Meta:
        model = UsersRooms
        fields = ['user_id', 'room_id','participate']
        
        """def create(self, validated_data):
            return super().create(validated_data)"""

    def update(self, instance, validated_data):
            instance.participate = validated_data.get('participate', instance.participate)
            instance.save()
            return instance
