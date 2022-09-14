from operator import truediv
from django.db import models


class Auth(models.Model):
    request_token = models.CharField(max_length=100, primary_key=True)
    request_secret = models.CharField(max_length=100)

    def __str__(self):
        return self.request_token

class Authenticated(models.Model):
    access_token = models.CharField(max_length = 128, primary_key=True)
    email = models.CharField(max_length=64)
    account_id = models.CharField(max_length=64)

# Adjust the foreign Key relationship to map the fields here to account_ids
class UserFavouriteAccounts(models.Model):
    account_id = models.CharField(max_length=64)
    favourited_id = models.CharField(max_length=64)

class Payload(models.Model):
    payload = models.TextField()
    response_status = models.IntegerField()

    class Meta:
        managed = False