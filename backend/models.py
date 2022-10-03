from email.policy import default
from operator import truediv
from django.db import models


class Auth(models.Model):
    twitter_session_id = models.CharField(max_length=100, default=None, primary_key=True)
    oauth_token = models.CharField(max_length=100, default=None)
    oauth_verifier = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.twitter_session_id

# class Authenticated(models.Model):
#     access_token = models.CharField(max_length = 128, primary_key=True)
#     email = models.CharField(max_length=64)
#     account_id = models.CharField(max_length=64)

# Adjust the foreign Key relationship to map the fields here to account_ids
class UserFavouriteAccounts(models.Model):
    twitter_session_id = models.ForeignKey("Auth", on_delete=models.CASCADE)
    favourited_id = models.CharField(max_length=64)

class Payload(models.Model):
    payload = models.TextField()
    response_status = models.IntegerField()

    class Meta:
        managed = False