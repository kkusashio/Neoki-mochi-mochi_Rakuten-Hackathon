from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EnrollInfoSerializer
from rest_framework.permissions import IsAuthenticated

class Enroll(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        print(request.auth)
        user=request.user
        print(user)
        info_data=dict(request.data)
        info_data["user"]=user.id
        print(info_data)
        serializer = EnrollInfoSerializer(data=info_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
