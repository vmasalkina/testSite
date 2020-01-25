from django.db import models
from django.conf import settings

class Data(models.Model):
    timestamp = models.DateTimeField()
    value = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)





