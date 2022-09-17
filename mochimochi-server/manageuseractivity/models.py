from django.db import models

class EnrollInformation(models.Model):
    user=models.ForeignKey('userauthentication.User', on_delete=models.CASCADE)
    date=models.DateTimeField()
