from django.db import models

class Data(models.Model):
    timestamp = models.DateTimeField()
    value = models.IntegerField()
    client = models.ForeignKey("Client", on_delete=models.CASCADE)

class Client(models.Model):
    last_modified = models.DateTimeField()
    token = models.TextField()
