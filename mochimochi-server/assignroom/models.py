from django.db import models
from userauthentication.models import User

# Create your models here.

class Rooms(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    zoom_url = models.CharField(max_length=100)
    user = models.ManyToManyField(User, through='UsersRooms',blank=True)
    class Meta:
        db_table = "rooms"

class UsersRooms(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    participate = models.BooleanField(default=False)
    class Meta:
        db_table = "userRoom"