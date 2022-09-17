import math
from django.shortcuts import render
from rest_framework.views import APIView	    # API
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import roomSerializer, userRoomSerializer
from .models import Rooms, UsersRooms
from .zoom import Zoom
from manageuseractivity.models import EnrollInformation
from userauthentication.models import User
from userauthentication.serializers import UserSerializer
from datetime import datetime
import re

class assignRoom(APIView):
    def post(self, request, format=None):
        date = request.data.get("date")
        # ユーザーの数を取得
        userNumber = EnrollInformation.objects.filter(date=date).count()
        print(userNumber)
        user_ids = list(EnrollInformation.objects.filter(date=date).values_list("user_id", flat=True))
        users=User.objects.filter(id__in=user_ids)
        # 部屋を作成
        assigned=0
        for _ in range(math.ceil(userNumber / 4)):
            n=self.roomUserNumCalc(userNumber)
            user_group=list(map(lambda x : x.id,users[assigned:assigned+n]))
            self.create_room(date,user_group)
            assigned += n
            userNumber -= n

        return Response(status=status.HTTP_200_OK)

    def create_room(self,date,user_groups):
        zoom = Zoom()
        zoom_url = zoom.create_room(date).get("join_url")
        data=dict()
        data["date"] = date
        data["zoom_url"] = zoom_url
        data["user"]=user_groups
        serializer = roomSerializer(data = data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return 
        else:
            print(serializer.errors)
            raise Exception("部屋の作成に失敗しました")
    
    def roomUserNumCalc(self, userNumber):
        if userNumber % 4 == 0:
            return 4
        elif userNumber % 4 == 1:
            return 5
        elif userNumber % 4 == 2:
            return 3
        elif userNumber % 4 == 3:
            return 3
    
class GetMeetingURL(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        user=request.user
        date=request.GET.get("date")
        try:
            int_date=list(map(int,re.split(r'T|-|:|Z|\.',date)[:-1]))
            int_date[3] += 1
            tomorrow="{}-{:02}-{:02}T{:02}:{:02}:{:02}Z".format(*int_date)
            room=Rooms.objects.get(user=user,date__range=[date,tomorrow])
            serializer=roomSerializer(room)
        except Rooms.DoesNotExist:
            return Response({'processed': False}, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        res=dict(serializer.data)
        res["proccessed"]=True
        return Response(res,status=status.HTTP_200_OK)
    
    
class ParticipateMeeting(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        user=request.user
        date=request.data.get("date")
        try:
            userRoom=UsersRooms.objects.get(user=user,room__date=date)
            print(userRoom)
            userRoom.participate=True
            userRoom.save()
            res={
                "user_id": userRoom.user.id,
                "room_id": userRoom.room.id,
                "participate": userRoom.participate
                }
            return Response(res,status=status.HTTP_200_OK)
        except:
            pass
        return Response(status=status.HTTP_400_BAD_REQUEST)