"""mochimochi-server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import rest_framework.authtoken.views as auth_views
from django.urls import include, path
from rest_framework import routers
from userauthentication.views import UserViewSet
from manageuseractivity.views import Enroll


from assignroom.views import ParticipateMeeting, assignRoom,GetMeetingURL

# Routers provide an easy way of automatically determining the URL conf.
authrouter = routers.DefaultRouter()
authrouter.register(r'signup', UserViewSet)



urlpatterns = [
    path('auth/', include(authrouter.urls)),
    path('auth/login/', auth_views.obtain_auth_token, name='login'),
    path('api/assign_room/', assignRoom.as_view(), name = "api"),
    path('meetings/', GetMeetingURL.as_view(), name = "get_meeting_url"),
    path('register/',Enroll.as_view(),name='register'),
    path('participate/',ParticipateMeeting.as_view(),name='participate'),
]
