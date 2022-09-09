from django.db import models

class Auth(models.Model):
    request_token = models.CharField(max_length=100, primary_key=True)
    request_secret = models.CharField(max_length=100)

    def __str__(self):
        return self.request_token

class Payload(models.Model):
    payload = models.TextField()
    responseStatus = models.IntegerField()

    class Meta:
        managed = False