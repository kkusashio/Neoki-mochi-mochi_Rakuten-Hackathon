from django.contrib.auth import get_user_model
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        try :
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_data=serializer.data
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)

        return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
